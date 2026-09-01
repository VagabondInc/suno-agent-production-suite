# Research Notes and Evidence Boundaries

Research refreshed 2026-09-01. Suno models and interfaces change frequently. This reference distinguishes product facts, third-party synthesis, and community experiments.

## Product Guidance

- Suno Custom mode separates user lyrics from Styles and Advanced options: https://help.suno.com/en/articles/3726721
- Suno's detailed-style guidance says newer models accept conversational arrangement descriptions rather than only short tag lists: https://help.suno.com/en/articles/5782849
- Suno's Creative Sliders expose Weirdness and Style Influence, with 50% Weirdness described as the normal midpoint: https://help.suno.com/en/articles/6141377
- Current 1000-character Style and 5000-character Lyrics limits are widely reported for v4.5/v5/v5.5, but the live UI remains authoritative: https://www.reddit.com/r/SunoAI/comments/1u9j24g/what_is_the_new_text_limit_for_simple_description/

## Community Tag Findings

- A community tag compilation reports `[Sting]`, `[Refrain]`, `[Big Finish]`, instrument cues, mood cues, modulation experiments, and EDM build/drop behavior. Replies also document ignored or accidentally sung tags: https://www.reddit.com/r/SunoAI/comments/1pap675/a_list_of_song_section_tags_to_help_improve_your/
- Users report composite headers such as `[Chorus - pitched vocal samples]`, voice-labeled verses, and stronger results when the same concept appears in both Style and Lyrics: https://www.reddit.com/r/SunoAI/comments/1hc0x2k/proper_metatag_structure_in_lyrics/
- A community guide explains the practical square-bracket/parentheses distinction, the need to leave instrumental sections lyric-free, and an A/B test method for tags: https://sunomarket.com/blog/suno-lyric-metatags-that-work
- Ending tags are repeatedly described as inconsistent across versions. `[End]`, `[Outro]`, `[Fade Out]`, and `[Big Finish]` are cues, not guarantees: https://www.reddit.com/r/SunoAI/comments/1d7fp7x/how_to_end_a_song_on_v35/

## Style and Fusion Findings

- Community users report that exact BPM, explicit ambience, and layered genre/instrument details reduce generic results: https://www.reddit.com/r/SunoAI/comments/1rv8q37/i_analyzed_100_suno_prompts_to_find_what_actually/
- A third-party guide recommends specific renderable descriptors, artist-free trait decomposition, and front-loading genre before era, production, voice, arrangement, dynamics, and tempo: https://sunomarket.com/guides/suno-prompts
- A fusion guide recommends one host genre plus two or three guest traits, with a single genre owning rhythm and tempo: https://sunomarket.com/blog/suno-genre-blending
- A community compendium distinguishes the global Style field from moment-to-moment Lyrics controls and catalogs structure, vocal, instrument, and production vocabulary: https://github.com/xerohour-ai/suno-forge/blob/main/suno-prompting-compendium.md

## Reported Experimental Combinations

Community experiments include vaporwave with barbershop harmony; drum-and-bass/ska with bagpipe leads; Gregorian chant, yodeling, and trap; mallsoft with nu-metal; baroque color in acid house; bluegrass techno; symphonic metal with Hawaiian folk instrumentation; cabaret hard rock; and metal with dark R&B/trap vocals. These are anecdotal starting points, not validated recipes:

- https://www.reddit.com/r/SunoAI/comments/1qk3w6l/what_unexpected_genre_combos_worked_insanely_well/
- https://www.reddit.com/r/SunoAI/comments/1q398go/create_a_new_genre_they_said/
- https://www.reddit.com/r/SunoAI/comments/1od4mf6/whats_the_most_unexpected_genre_mashup_youve/

One experimental user describes intentionally conflicting genre/language contexts, concept-album continuity, and organic audio seeds as ways to push beyond commercial defaults: https://www.reddit.com/r/SunoAI/comments/1tzyneb/crazy_accidental_or_intended_experimental_results/

## Interpretation Rules

- Suno publishes no complete guaranteed bracket-tag specification.
- `Core`, `community-reported`, and `experimental` labels describe evidence strength, not certainty.
- A tag that worked in one model, genre, or account configuration may fail in another.
- Do not state that a tag, fusion, slider percentage, field limit, two-variation result, or download format is confirmed-current without checking the live interface.
- The corpus is for original music. Never emulate a living artist by name; decompose desired traits into genre, instrumentation, arrangement, vocal behavior, and production language.
