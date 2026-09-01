---
name: fal-music-video-builder
description: Design, validate, and import a budget-aware fal.ai workflow for a complete music video when the user has a finished song and wants multi-agent story, continuity, shot, image, motion, timing, and workflow development.
---

# fal.ai Music Video Builder

Create an importable fal.ai workflow whose visual timeline covers the entire source song plus a 2–5 second visual tail. The workflow must use the user's original song as soundtrack, stay within the approved budget including retry reserve, and preserve character, wardrobe, prop, location, and visual-world continuity.

This is a delegated production workflow. Use spawned subagents for the creative and technical specialist contracts in [agent-production-pipeline.md](references/agent-production-pipeline.md). The root agent coordinates, resolves interfaces, and accepts/rejects artifacts; it must not replace all specialist passes with one monolithic draft. If subagents are unavailable, explain that the requested execution contract cannot be met and do not present a single-agent build as compliant.

## Required preflight

1. Obtain the absolute local song path, canonical lyrics, style/production direction, desired aspect ratio and resolution, intended audience/content limits, available character/prop/location references, and a hard budget in USD. Ask for the budget before selecting models.
2. Run `scripts/probe_audio.py /absolute/path/song.ext` and retain the exact decimal duration. Do not round early.
3. Set the visual target at song duration + 3 seconds, then solve with current model duration constraints so the final sum is at least +2 and at most +5 seconds. Never shorten below the song.
4. Reserve 15–20% of the budget for retries. First-pass planned spend must fit the remainder.
5. Discover current fal models and retrieve official OpenAPI schemas for every chosen endpoint from `https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=<encoded-endpoint>`. Verify field names, types, duration enums/ranges, output paths, resolution, aspect ratio, and current pricing. Do not trust a cached model list when live evidence is available.
6. Use video generation with native audio disabled unless there is a documented creative reason; the final soundtrack is the original song.

Read [fal-workflow-contract.md](references/fal-workflow-contract.md) before constructing JSON. It incorporates the complete functional constraints of the existing `$fal-workflow` skill in original, redistributable form. Read [model-and-budget-policy.md](references/model-and-budget-policy.md) for model selection and cost evidence.

## Production and acceptance

Run the specialists in dependency waves, with no more concurrent children than the environment permits. Persist each handoff artifact as JSON. A downstream role may reject malformed or incomplete upstream work, but may not silently rewrite its creative contract.

After the workflow architect produces the JSON, run:

```bash
python3 scripts/validate_music_video.py \
  --plan /absolute/path/production-plan.json \
  --workflow /absolute/path/workflow.json \
  --schema-catalog /absolute/path/live-schema-catalog.json
```

Proceed only on `PASS`. Independently audit timing, budget, continuity, node structure, references, dependencies, model parameters, ordered merge, original-audio merge, and final output. Syntax validity alone is not sufficient.

## Browser import

Use `$computer-use:computer-use`; read its `SKILL.md` completely first. Navigate to `https://fal.ai/workflows`, inspect current UI state, choose the current **Create Workflow** path, open the overflow menu, choose **Import Workflow**, and select the validated local JSON.

The user must be logged into fal.ai. If the authenticated workflow workspace is not visible, stop, ask the user to log in manually, and say: `Once you are logged into fal.ai, reply continue and I will resume.` Do not request or handle credentials or verification codes.

Uploading the JSON is an external file transmission. Confirm immediately before upload unless the current user request explicitly authorized uploading that exact file to fal.ai. Verify the imported workflow renders, its inputs and nodes are present, and visible validation errors are absent. Do not click **Run** or trigger paid generation. Tell the user: `The validated fal.ai music-video workflow is imported and ready. Please review the cost and click Run when you are ready.`
