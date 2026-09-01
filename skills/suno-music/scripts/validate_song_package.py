#!/usr/bin/env python3
"""Validate Suno style and lyric field invariants."""

from __future__ import annotations

import argparse
from pathlib import Path


def read_value(text: str | None, path: Path | None) -> str:
    if path is not None:
        value = path.read_text(encoding="utf-8")
    elif text is not None:
        value = text
    else:
        raise ValueError("provide text or a file")
    return value[:-1] if value.endswith("\n") else value


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Suno song package.")
    style = parser.add_mutually_exclusive_group(required=True)
    style.add_argument("--style")
    style.add_argument("--style-file", type=Path)
    lyrics = parser.add_mutually_exclusive_group(required=True)
    lyrics.add_argument("--lyrics")
    lyrics.add_argument("--lyrics-file", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--excluded-styles", required=True)
    parser.add_argument("--weirdness", required=True, type=int)
    parser.add_argument("--style-influence", required=True, type=int)
    args = parser.parse_args()

    style_text = read_value(args.style, args.style_file)
    lyrics_text = read_value(args.lyrics, args.lyrics_file)
    errors: list[str] = []

    if len(style_text) != 1000:
        errors.append(f"style is {len(style_text)} characters; expected exactly 1000")
    if "\n" in style_text or "\r" in style_text:
        errors.append("style contains a line break")
    if len(lyrics_text) > 5000:
        errors.append(f"lyrics are {len(lyrics_text)} characters; maximum is 5000")
    if not args.title.strip():
        errors.append("title is empty")
    if not args.excluded_styles.strip():
        errors.append("excluded styles is empty")
    if not 0 <= args.weirdness <= 80:
        errors.append("weirdness must be between 0 and 80")
    if not 25 <= args.style_influence <= 100:
        errors.append("style influence must be between 25 and 100")

    if errors:
        for error in errors:
            print(f"INVALID: {error}")
        return 1

    print(
        f"VALID: style={len(style_text)} characters; "
        f"lyrics={len(lyrics_text)} characters; weirdness={args.weirdness}; "
        f"style_influence={args.style_influence}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
