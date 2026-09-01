# Suno Style Syntax

Use this guide to turn the 1000-character requirement into a precise production brief. The limit is a ceiling in Suno; this skill deliberately fills it exactly because that is the product contract. Every character should add control rather than filler.

## Field Separation

- **Style field:** global sonic identity—genre, rhythm, tempo, instrumentation, vocals, mood, arrangement arc, production, and mix.
- **Lyrics field:** words to be sung plus square-bracketed section and performance cues.
- **Parentheses in Lyrics:** audible backing vocals, echoes, responses, or ad-libs.
- **Exclude field:** unwanted genres, instruments, vocal behaviors, or production traits when Suno exposes that control. Do not consume Style space with exclusions unless the UI lacks a dedicated field.

## 1000-Character Production Brief

Write one paragraph in this order, using compact sentences or semicolon-separated clauses:

1. **Identity:** primary genre first, then one subgenre or experimental frame.
2. **Pulse:** exact BPM or tempo feel, meter, swing, subdivision, drum architecture, and bass relationship.
3. **Harmony:** key/mode if useful, chord color, harmonic rhythm, dissonance, or tonal movement.
4. **Palette:** name instruments and assign roles—lead, counterline, rhythm, bass, texture, punctuation.
5. **Voice:** range, timbre, diction, register, phrasing, emotion, ensemble role, and vocal effects.
6. **Form:** opening state, verse density, chorus expansion, contrast section, climax, and ending behavior.
7. **Production:** era, recording space, saturation, distortion, editing, stereo depth, reverb/delay, and transient character.
8. **Mix priorities:** what stays foregrounded, what remains sparse, how the low end behaves, and how dynamics evolve.

Front-load non-negotiables. Use renderable musical language such as `174 BPM rolling jungle breaks`, `close-miked contralto with dry consonants`, or `prepared-piano attacks feeding granular delays`; avoid empty language such as `amazing`, `masterpiece`, `viral`, or `professional quality`.

## Fusion Hierarchy

Treat a fusion as one host grammar with guest traits:

`host genre + host pulse/form + two or three guest traits + unifying production logic`

Let the host own rhythm and form. Borrow a guest instrument, harmonic vocabulary, vocal technique, or recording texture. Avoid asking two rhythmically dominant genres to control the groove simultaneously. If three sources are involved, keep one genre label and express the other two as concrete timbres or techniques.

Example architecture:

`Electroacoustic IDM is the host; fractured 92 BPM breaks and asymmetrical phrase lengths control the form. A bass clarinet borrows free-jazz multiphonics, while prepared piano and tape-spliced room noise supply musique-concrete texture...`

## Contradiction Check

Resolve conflicts before writing:

- One tempo wins; do not combine incompatible implied tempos without naming a half-time/double-time relationship.
- One low-end source dominates; do not stack wobble bass, 808 sub, and distorted bass guitar without assigning sections or frequency roles.
- One space dominates per section; `bone-dry close vocal` and `cathedral wash` can coexist only when the transition is intentional.
- One density state applies at a time; describe a sparse verse that expands into a lush chorus rather than asking for both globally.
- Use artist-free traits. Describe era, instrumentation, vocal behavior, arrangement, and production instead of naming a living or recognizable artist.

## Character-Fitting Method

Draft for substance, then count with `scripts/validate_song_package.py`.

- If short, add missing articulation, spatial placement, transition behavior, harmonic movement, vocal phrasing, or mix priorities.
- If long, remove duplicated adjectives, articles, generic transitions, and low-priority gear names.
- Never pad with repeated phrases, fake technical jargon, quality claims, or invisible whitespace.
- Preserve one paragraph and revalidate after every edit.

## Lyrics Formatting

Use section tags on their own lines, with a blank line before each new section. Composite headers may carry a few local cues:

```text
[Verse 1: close-miked alto | clipped phrasing | sparse kick]
Lyric line
Lyric line

[Chorus: stacked harmony | full sub | widened drums]
Hook line
(echoed response)
```

Keep local instructions compact and reinforce crucial cues in the Style field. If a direction is ignored, move it to the Style field or simplify the header; do not multiply tags blindly.

## Iteration Discipline

Suno output is stochastic. For a clean tag experiment, compare two otherwise identical generations with one cue added or removed. Listen for the promised change. If it is absent, treat the tag as ineffective for that model/style combination. Do not spend credits on repeated retries without user authorization.
