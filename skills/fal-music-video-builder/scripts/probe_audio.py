#!/usr/bin/env python3
"""Print exact audio duration as JSON using ffprobe, with afinfo fallback."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from decimal import Decimal, InvalidOperation
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", type=Path)
    args = parser.parse_args()
    path = args.audio.expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f"Audio file not found: {path}")
    duration = None
    source = None
    if shutil.which("ffprobe"):
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)],
            check=True, capture_output=True, text=True,
        )
        duration = Decimal(json.loads(result.stdout)["format"]["duration"])
        source = "ffprobe"
    elif shutil.which("afinfo"):
        result = subprocess.run(["afinfo", str(path)], check=True, capture_output=True, text=True)
        match = re.search(r"estimated duration:\s*([0-9.]+)\s*sec", result.stdout)
        if not match:
            raise SystemExit("afinfo did not report an estimated duration")
        duration = Decimal(match.group(1))
        source = "afinfo"
    else:
        raise SystemExit("Neither ffprobe nor afinfo is available")
    try:
        if duration <= 0:
            raise InvalidOperation
    except InvalidOperation as exc:
        raise SystemExit("Invalid non-positive duration") from exc
    print(json.dumps({"path": str(path), "duration_seconds": str(duration), "probe": source}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
