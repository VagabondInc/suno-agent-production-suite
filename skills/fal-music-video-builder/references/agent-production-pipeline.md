# Multi-Agent Production Pipeline

The root agent owns the schedule, file contracts, budget boundary, and final acceptance. With three child slots, run these roles in waves and reuse agents only when their prior role is complete.

## Wave 1: meaning and world

### Audio analyst

Input: audio, canonical lyrics, production direction. Output: `song-map.json` with exact duration, section timestamps, vocal entrances, instrumental passages, tempo/meter estimates, downbeat and transition landmarks, dynamic curve, lyrical turns, and confidence notes. Do not invent unreadable lyrics.

### Narrative architect

Input: song-map and lyrics. Output: `story-bible.json` with a causal three-act premise, protagonist want/obstacle/change, recurring motif whose meaning evolves, opening/final image relationship, section-to-story mapping, and exclusions. Reject literal lyric illustration, generic montage, and interchangeable redemption arcs.

### Visual-world designer

Input: song-map, story-bible, style. Output: `continuity-bible.json` containing stable IDs and exact descriptions for characters, faces, body traits, wardrobe states, props, locations, era, materials, palette, light, lenses, texture, aspect ratio, and prohibited drift. Include reference-image provenance and consent status.

## Wave 2: edit and economics

### Editorial scene planner

Input: song/story/continuity bibles. Output: `scene-plan.json`. Every scene has exact in/out, narrative purpose, entry/exit state, location, character/prop IDs, musical sync point, transition, and visual change. Cover the complete target duration without unintended gaps.

### Model and budget producer

Input: hard budget, duration, output spec. Output: `model-plan.json` and `live-schema-catalog.json`. Query official current schemas and pricing. Record endpoint IDs, timestamp, URLs, accepted clip durations, field names, outputs, per-call/per-second costs, generation counts, and 15–20% retry reserve. Select the least expensive coherent plan that can meet the creative brief; surface compromises before locking them.

### Continuity editor

Input: prior artifacts. Output: `continuity-audit.json`. Detect identity drift, impossible geography, wardrobe/prop discontinuity, repeated compositions, and visual rules that conflict with the narrative.

## Wave 3: shots and prompts

### Shot designer

Output: `shot-plan.json`. Each clip has stable ID, scene ID, exact timeline in/out and schema-supported duration, framing, lens, camera height/path, blocking, subject action, start/end composition, transition, continuity IDs, and musical cue. One achievable primary motion per clip.

### Frame-prompt specialists

Partition scenes across agents. For each scene produce a scene-overview image prompt, canonical character and prop references, a start-frame prompt, optional end-frame prompt, and image-to-image prompts for alternate angles. Every prompt restates required continuity IDs and separates invariant identity from shot-specific changes.

### Motion-prompt specialists

Partition scenes across agents. Produce one image-to-video prompt per shot: subject action, camera motion, environmental motion, timing beats, physical constraints, end state, negative constraints, and only live-schema-supported parameters. Do not ask the model to perform multiple incompatible actions in one short clip.

## Wave 4: assembly

### Workflow architect

Input: all accepted artifacts. Output: `production-plan.json` and importable workflow JSON. Build image/reference nodes, shot images, video nodes, ordered merge, original-song audio merge, and display output. Preserve creative decisions; flag incompatibilities.

### Independent audit trio

- Structure auditor: JSON envelope, node types/IDs, dependencies, references, schemas, output paths.
- Timing auditor: exact coverage, supported clip durations, no gaps/unintended overlaps, +2–5 second tail.
- Cost/continuity auditor: budget plus reserve, current pricing evidence, retry count, native-audio waste, identity/wardrobe/prop/location continuity.

The root accepts only when all three return `PASS`. Store reasons and corrections for any rejection.
