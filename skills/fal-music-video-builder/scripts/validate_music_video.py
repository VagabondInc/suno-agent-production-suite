#!/usr/bin/env python3
"""Validate timing, budget, continuity, schema evidence, and fal workflow structure."""

from __future__ import annotations

import argparse
import json
import re
from decimal import Decimal
from pathlib import Path
from typing import Any

REF = re.compile(r"^\$(input|[A-Za-z0-9_-]+)(?:\.[A-Za-z0-9_-]+)+$")

def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), parse_float=Decimal)

def walk(value: Any):
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)
    elif isinstance(value, str):
        yield value

def validate_refs(value: Any, consumer: str, depends: set[str], nodes: dict[str, Any], catalog: dict[str, Any], errors: list[str]) -> None:
    for item in walk(value):
        if "$" in item and not REF.fullmatch(item):
            errors.append(f"mixed or invalid reference in {consumer}: {item}")
            continue
        match = REF.fullmatch(item)
        if not match or match.group(1) == "input":
            continue
        source = match.group(1)
        if source not in nodes:
            errors.append(f"{consumer} references unknown node {source}")
            continue
        if source not in depends:
            errors.append(f"{consumer} references {source} without dependency")
        source_app = nodes[source].get("app")
        allowed_outputs = set(catalog.get(source_app, {}).get("output_paths", []))
        output_path = item.split(".", 1)[1]
        if allowed_outputs and output_path not in allowed_outputs:
            errors.append(f"{consumer} uses unverified output path for {source_app}: {output_path}")

def validate_plan(plan: dict[str, Any], errors: list[str]) -> None:
    song = Decimal(str(plan.get("song_duration_seconds", 0)))
    visual = Decimal(str(plan.get("visual_duration_seconds", 0)))
    clips = plan.get("clips", [])
    total = sum((Decimal(str(c.get("duration_seconds", 0))) for c in clips), Decimal("0"))
    if not song > 0:
        errors.append("song_duration_seconds must be positive")
    if not song + Decimal("2") <= visual <= song + Decimal("5"):
        errors.append("visual duration must be song duration plus 2 to 5 seconds")
    if abs(total - visual) > Decimal("0.001"):
        errors.append("clip durations do not sum to visual_duration_seconds")
    cursor = Decimal("0")
    seen = set()
    for clip in sorted(clips, key=lambda c: Decimal(str(c.get("start_seconds", 0)))):
        cid = clip.get("id")
        start = Decimal(str(clip.get("start_seconds", 0)))
        duration = Decimal(str(clip.get("duration_seconds", 0)))
        if cid in seen or not cid:
            errors.append(f"invalid or duplicate clip id: {cid}")
        if duration <= 0:
            errors.append(f"{cid} duration must be positive")
        seen.add(cid)
        if abs(start - cursor) > Decimal("0.001"):
            errors.append(f"timeline gap or overlap before {cid}")
        cursor = start + duration
        if not clip.get("continuity_ids"):
            errors.append(f"{cid} has no continuity_ids")
        if clip.get("generate_audio") not in (False, None):
            errors.append(f"{cid} enables native audio")
    budget = Decimal(str(plan.get("budget_usd", 0)))
    cost = Decimal(str(plan.get("planned_cost_usd", 0)))
    reserve = Decimal(str(plan.get("retry_reserve_usd", 0)))
    if budget <= 0 or cost + reserve > budget:
        errors.append("planned cost plus retry reserve exceeds or lacks budget")
    if reserve < budget * Decimal("0.15"):
        errors.append("retry reserve is below 15% of budget")
    if not plan.get("final_duration_strategy_verified"):
        errors.append("final merge duration behavior is not verified")
    if not plan.get("final_duration_evidence_url"):
        errors.append("final merge duration evidence URL is missing")
    if not plan.get("schema_checks"):
        errors.append("no live schema checks recorded")

def validate_workflow(workflow: dict[str, Any], catalog: dict[str, Any], errors: list[str]) -> None:
    contents = workflow.get("contents")
    if not isinstance(contents, dict):
        errors.append("workflow lacks contents object")
        return
    nodes = contents.get("nodes", {})
    if not isinstance(nodes, dict) or not nodes:
        errors.append("contents.nodes must be a non-empty object")
        return
    for key, node in nodes.items():
        if node.get("id") != key:
            errors.append(f"node key/id mismatch: {key}")
        if node.get("type") not in {"run", "display"}:
            errors.append(f"invalid node type: {key}")
        depends = set(node.get("depends", []))
        validate_refs(node.get("input", {}), key, depends, nodes, catalog, errors)
        validate_refs(node.get("fields", {}), key, depends, nodes, catalog, errors)
        if node.get("type") == "run":
            app = node.get("app")
            schema = catalog.get(app)
            if not schema:
                errors.append(f"no live schema catalog entry for {app}")
            else:
                if not schema.get("source_url") or not schema.get("verified_at"):
                    errors.append(f"schema evidence incomplete for {app}")
                allowed = set(schema.get("allowed_inputs", []))
                if allowed:
                    unknown = set(node.get("input", {})) - allowed
                    if unknown:
                        errors.append(f"unsupported inputs for {app}: {sorted(unknown)}")
                for field, allowed_values in schema.get("allowed_values", {}).items():
                    value = node.get("input", {}).get(field)
                    if value is not None and not (isinstance(value, str) and value.startswith("$")) and value not in allowed_values:
                        errors.append(f"unsupported value for {app}.{field}: {value}")
                missing = set(schema.get("required_inputs", [])) - set(node.get("input", {}))
                if missing:
                    errors.append(f"missing required inputs for {app}: {sorted(missing)}")
    schema_input = contents.get("schema", {}).get("input", {})
    for field, spec in schema_input.items():
        if spec.get("modelId") not in nodes:
            errors.append(f"schema input {field} has invalid modelId")
    display_ids = {key for key, node in nodes.items() if node.get("type") == "display"}
    output_deps = set().union(*(set(nodes[key].get("depends", [])) for key in display_ids)) if display_ids else set()
    validate_refs(contents.get("output", {}), "contents.output", output_deps, nodes, catalog, errors)

    merge_video = [k for k, n in nodes.items() if str(n.get("app", "")).endswith("/merge-videos")]
    merge_audio = [k for k, n in nodes.items() if str(n.get("app", "")).endswith("/merge-audio-video")]
    if not merge_video:
        errors.append("workflow lacks ordered merge-videos node")
    if not merge_audio:
        errors.append("workflow lacks original-song merge-audio-video node")
    if "song_audio_url" not in schema_input:
        errors.append("workflow lacks song_audio_url input")

def cross_validate(plan: dict[str, Any], workflow: dict[str, Any], catalog: dict[str, Any], errors: list[str]) -> None:
    nodes = workflow.get("contents", {}).get("nodes", {})
    for clip in plan.get("clips", []):
        node = nodes.get(clip.get("id"))
        if not node:
            errors.append(f"planned clip missing from workflow: {clip.get('id')}")
            continue
        if clip.get("model_app") != node.get("app"):
            errors.append(f"model mismatch for {clip.get('id')}")
        node_duration = node.get("input", {}).get("duration")
        if node_duration is None or Decimal(str(node_duration)) != Decimal(str(clip.get("duration_seconds"))):
            errors.append(f"duration mismatch for {clip.get('id')}")
        aspect = plan.get("aspect_ratio")
        node_aspect = node.get("input", {}).get("aspect_ratio")
        if node_aspect is not None and node_aspect != aspect:
            errors.append(f"aspect ratio mismatch for {clip.get('id')}")
    computed = Decimal("0")
    for node in nodes.values():
        if node.get("type") != "run":
            continue
        rate = catalog.get(node.get("app"), {})
        computed += Decimal(str(rate.get("rate_usd_per_call", 0)))
        if "duration" in node.get("input", {}):
            computed += Decimal(str(rate.get("rate_usd_per_second", 0))) * Decimal(str(node["input"]["duration"]))
    declared = Decimal(str(plan.get("planned_cost_usd", 0)))
    if abs(computed - declared) > Decimal("0.01"):
        errors.append(f"planned cost does not match workflow-derived cost: {computed}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--workflow", required=True, type=Path)
    parser.add_argument("--schema-catalog", required=True, type=Path)
    args = parser.parse_args()
    errors: list[str] = []
    try:
        plan, workflow, catalog = load(args.plan), load(args.workflow), load(args.schema_catalog)
        validate_plan(plan, errors)
        validate_workflow(workflow, catalog, errors)
        cross_validate(plan, workflow, catalog, errors)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        errors.append(f"parse/validation error: {exc}")
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
