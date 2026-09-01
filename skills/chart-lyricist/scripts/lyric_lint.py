#!/usr/bin/env python3
"""Flag prohibited and high-risk generic lyric language."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

HARD_PATTERNS = {
    "velvet skies": r"\bvelvet\s+sk(?:y|ies)\b",
    "streetlight": r"\bstreet[ -]?lights?\b",
    "bruised": r"\bbruis(?:e|ed|es|ing)\b",
    "neon/city lights": r"\b(?:neon|city)\s+lights?\b|\bneon\s+glow\b",
    "shadow cliche": r"\b(?:dancing|chasing)\s+shadows?\b",
    "echo cliche": r"\b(?:fading\s+)?echo(?:es)?\s+(?:of|in)\s+(?:the\s+)?(?:past|night)\b|\byour\s+echo\b",
    "whispered wind": r"\bwhispers?\s+in\s+the\s+wind\b|\bwhispered\s+by\s+the\s+wind\b",
    "ashes/phoenix": r"\brise\s+from\s+the\s+ashes\b|\blike\s+a\s+phoenix\b",
    "veins cliche": r"\b(?:fire|ice)\s+in\s+my\s+veins\b",
    "chains cliche": r"\b(?:break|breaking)\s+(?:these|the|my|your)\s+chains\b|\bchains?\s+that\s+bind\b",
    "sky/horizon cliche": r"\b(?:edge\s+of\s+dawn|endless\s+sky|open\s+sky|painted\s+sk(?:y|ies)|chasing\s+the\s+horizon)\b",
    "stock burden/time": r"\bweight\s+of\s+the\s+world\b|\bfrozen\s+in\s+time\b",
    "stock conflict": r"\bdemons?\s+in\s+my\s+head\b|\bcalm\s+before\s+the\s+storm\b",
    "stock permanence/mystery": r"\bcarved\s+in\s+stone\b|\bstor(?:y|ies)\s+untold\b|\bbroken\s+pieces\b",
}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    text = args.file.read_text(encoding="utf-8")
    failures = []
    for label, pattern in HARD_PATTERNS.items():
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            line = text.count("\n", 0, match.start()) + 1
            failures.append(f"line {line}: {label}: {match.group(0)!r}")
    if failures:
        print("FAIL: prohibited or stock lyric language detected")
        print("\n".join(failures))
        return 1
    print("PASS: no hard-banned lyric language detected")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
