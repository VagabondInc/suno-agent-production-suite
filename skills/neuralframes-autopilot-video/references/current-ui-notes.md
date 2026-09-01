# NeuralFrames Autopilot UI Notes

Official documentation reviewed 2026-09-01 describes four stages: Music, Track, Storyboard, and Video.

- Music: Upload Music opens the operating-system file picker.
- Track: waveform, Lyric Editor, Aspect Ratio, Duration Preset, Character, Video Concept, Visual Style, and Personalize controls.
- Character: Auto, No Character, New Character by prompt or upload, and previous characters; current documentation supports up to three selected characters. Name generated/uploaded characters and apply the selection. `No Character` does not necessarily exclude humans; use `NO: Characters NO: Humans` in the concept when needed.
- Visual Style: preset or trained styles with previews. Changing concept, style, or character after storyboard generation can require Regenerate Scenes and consume credits.
- Lyrics: transcription is automatic but editable; compare text and timestamps to the canonical lyrics.
- Final action: current docs call it Create Video and offer techniques such as Classic Video, Lyric Showcase, or Vocal Video. Generation can begin immediately, consume credits, and cannot necessarily be interrupted.

Do not hard-code element indexes or assume older labels such as Save, Select Style, or Create Project still exist. Inspect current controls semantically.

## Sources

- NeuralFrames, [The Four Stages of Autopilot](https://help.neuralframes.com/en/articles/12038142-handbook-the-four-stages-of-autopilot)
- NeuralFrames, [Intro to Autopilot](https://help.neuralframes.com/en/articles/12022753-intro-to-autopilot)
- NeuralFrames, [Multiple Character Consistency](https://help.neuralframes.com/en/articles/12022762-what-is-multiple-character-consistency)
- NeuralFrames, [Autopilot Styles](https://help.neuralframes.com/en/articles/12022513-what-are-autopilot-styles)
- NeuralFrames, [Credit Usage](https://help.neuralframes.com/en/articles/10507175-how-are-credits-used-for-each-tool)
- NeuralFrames, [Autopilot feature overview](https://www.neuralframes.com/features/autopilot)
- Secondary UI walkthrough, [AI Musicpreneur](https://www.aimusicpreneur.com/ai-tools-news/how-to-make-ai-music-videos-with-neural-frames/)

Recheck the live site and official documentation because labels, presets, models, pricing, and credit behavior can change.
