---
name: neuralframes-autopilot-video
description: Build a cinematic NeuralFrames Autopilot music-video scaffold in the browser when the user has a finished song and wants its audio, lyrics, narrative concept, character, duration, and visual style configured for review.
---

# NeuralFrames Autopilot Music Video Creator

Use `$computer-use:computer-use` for every browser interaction. Read its `SKILL.md` completely before operating the UI. Navigate to `https://neuralframes.com/songs?via=chatgpt` in the default browser and derive fresh accessibility state after every action; current labels can differ from older screenshots or instructions.

## Inputs and preflight

Obtain the local song path, canonical lyrics, Suno style/production direction, desired aspect ratio, and any approved character image. Confirm that the selected audio is the intended final song. The user must be logged into NeuralFrames. If the authenticated workspace is not visible, stop, ask the user to log in manually, and say: `Once you are logged into NeuralFrames, reply continue and I will resume.` Do not request or handle credentials or verification codes.

Before uploading audio, confirm at action time unless the current user request explicitly authorized uploading that exact song to NeuralFrames. A personal photograph is sensitive data: confirm the exact image and NeuralFrames destination immediately before upload, and do not upload another person's likeness without the user's assurance of permission.

## Cinematic concept

Develop a complete visual treatment from the lyrics and sound:

- one-sentence visual thesis and a three-act cause-and-effect arc;
- recurring protagonist, object, location, gesture, or metaphor whose meaning changes;
- one deliberately unusual visual rule involving era, wardrobe, material, scale, process, camera grammar, or art direction;
- section-specific escalation tied to musical events rather than literal line-by-line illustration;
- a final image that resolves or productively complicates the opening image;
- explicit exclusions using `NO: subject` when needed.

Reject generic performance montages, interchangeable romance imagery, random spectacle, predictable rise/fall redemption, and concepts that merely restate the lyrics. Keep character, wardrobe, prop, palette, and location continuity explicit.

## Browser workflow

1. Inspect the current Music page and choose **Upload Music**. Upload the approved song.
2. On the Track page, find the Video Concept control and enter the complete treatment. Use the current save/apply control if present.
3. Set **Duration Preset** to **Full**. Do not silently choose a shorter excerpt.
4. Under Character, choose the add control. If an approved image exists, choose the current upload-new-character path, upload it, name the character, and apply/approve it. Otherwise choose the describe/new-character path, write a distinctive character specification matching the concept and genre, generate candidates, inspect them, and approve only a coherent identity.
5. Open Visual Style. Read every currently visible style name and inspect its thumbnail. Select the style that best supports the concept, genre, character fidelity, and final aspect ratio. For a realistic uploaded person, consider no preset style when a preset materially harms resemblance.
6. Wait for lyric detection. Compare the detected words and ordering against the canonical lyrics. Correct the lyric editor and timestamps when supported. If a material mismatch cannot be corrected, stop and report it.
7. Reinspect all configured fields: full duration, concept, character selection, style, aspect ratio, lyrics, and any visible credit estimate.

Current official guidance uses **Create Video** where older UI descriptions used **Create Project**. Treat either as the final generation control. Clicking a generation option can consume credits immediately and may be impossible to pause or cancel. Do not click it without explicit action-time confirmation after showing the visible credit estimate and chosen technique. If the request is only to build the scaffold, stop before this control and say: `The NeuralFrames video scaffold is ready. Please take over in the browser to review and generate it.`

Read [current-ui-notes.md](references/current-ui-notes.md) before operating the site.
