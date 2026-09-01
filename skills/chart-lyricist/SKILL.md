---
name: chart-lyricist
description: Write and rigorously revise distinctive, performance-ready song lyrics and production cues when the user wants premium songwriting, a lyric rewrite, a stronger hook, less generic language, or chart-caliber craft without imitating a living artist.
---

# Chart Lyricist

Build songs with professional workshop discipline: a specific dramatic premise, sensory evidence, singable prosody, structural escalation, a memorable but non-obvious hook, and production cues that reinforce the lyric. Aim for the craft standards associated with acclaimed commercial songwriting; never promise awards, chart placement, or commercial success.

## Required Process

1. Establish the singer, addressee, immediate situation, want, obstacle, consequence, point of view, time frame, genre, tempo, vocal identity, and content boundaries. Infer reversible details; ask only when a missing choice would materially change the song.
2. Write a private one-sentence dramatic contract and several hook/title candidates. Reject any candidate that could be pasted unchanged into hundreds of songs.
3. Before drafting, build a private sensory bank of at least 20 concrete nouns, actions, habits, transactions, overheard phrases, location facts, and physical consequences. Use multiple senses and movement.
4. Map what changes in every section: new information, pressure, power, time, point of view, or consequence. A second verse cannot merely paraphrase the first.
5. Draft in conversational syntax with active verbs, observable behavior, subtext, and controlled repetition. Make meaning clear without explaining every implication.
6. Fit language to music: natural spoken stresses land on strong beats, vowels remain singable, line lengths and rhyme density serve momentum, and the chorus earns its lift.
7. Run [anti-cliche-standard.md](references/anti-cliche-standard.md), then run `scripts/lyric_lint.py` on the final lyric text. Rewrite every hard failure; do not merely disclose it.
8. Run four adversarial revisions: listener clarity, singer authenticity, editor economy, and producer/prosody. Keep a line only if it advances scene, character, hook, sound, or turn.

Read [workshop-craft.md](references/workshop-craft.md) for the research-backed methods. Read [production-tags.md](references/production-tags.md) when writing square-bracket cues. When producing a complete Suno package, also follow `$suno-music`; its exact output limits remain controlling.

## Non-Negotiable Originality

- Never use `velvet skies`, `streetlight` or `streetlights`, or `bruised` in any lyric.
- Do not use decorative neon/night imagery, dancing shadows, echoes as memory shorthand, whispered wind, phoenix/ashes uplift, chains-to-freedom, fire-in-veins, generic storms, or unexplained cosmic transcendence.
- A ban is not satisfied by swapping one stock noun for another. Replace the entire thought with character-specific evidence.
- Do not force inversion, antique diction, vague pronouns, convenient perfect rhymes, symmetrical filler, or generic outro affirmations.
- Do not imitate a named living artist. Translate references into high-level traits such as density, restraint, narrative distance, rhythmic placement, or harmonic tension.

## Production Tags

Tags are arrangement cues, not decorations. Put each square-bracket direction on its own line and make it describe an audible change: section function, vocal delivery, instrumentation, dynamics, texture, meter, or transition. Never pack a paragraph into one tag or use tags to compensate for weak writing. Treat model response as probabilistic.

## Delivery

Unless another skill defines a stricter format, return exactly `Production Direction` and `Tagged Lyrics`. Separate lyric sections with blank lines. Do not expose private brainstorming, scoring, or revision notes unless requested.
