# fal.ai Workflow Contract

This is the functional contract incorporated from the pre-existing fal workflow skill. It replaces copied third-party prose and examples with an original, distributable specification.

## Envelope

An importable workflow has top-level metadata and a `contents` object. `contents` contains `name`, `nodes`, `output`, `schema`, `version`, and `metadata`. Define user inputs only in `contents.schema.input`; never create an input node.

Only two node types are valid:

- `run` executes a fal model or utility.
- `display` exposes results.

Every node object key must equal its `id` exactly. Use `depends`, not `dependsOn`.

## References

References use whole-string values such as `$input.prompt`, `$shot-01.images.0.url`, `$clip-01.video.url`, `$merge.video.url`, or `$analysis.output`. Never combine prose and a variable in one string. To combine text, use a currently available fal text-concat or merge-text endpoint verified by live schema.

Every `$node...` reference requires that node ID in the consumer's `depends`. Every display node and final output must depend on all nodes it references. Every input schema field needs a `modelId` naming a real consuming run node.

Use a text-only router for text; use a vision router only when sending images. Verify current app IDs and output paths through official OpenAPI before authoring references.

## Music-video patterns

- Fan out independent frame/video generations from accepted shared inputs; do not serialize unrelated shots.
- For continuity extension, extract the previous clip's last frame or use a schema-supported explicit end frame.
- First/last-frame generation requires both referenced frame nodes in `depends`.
- Merge videos in editorial order, then merge the original song audio. Do not generate replacement music.
- Final display and `contents.output` expose the assembled video and, when helpful, intermediate shots for review.

## Legacy warning

Do not use builders that emit `_type: ComfyApp`, top-level `nodes`, or `dependsOn`. Those shapes conflict with the current import contract represented here. Use the validator supplied by this skill and verify against the live fal importer.

## Required checks

- JSON parses.
- Node types are only `run` or `display`.
- Node key equals `id`.
- No mixed string interpolation.
- Every node reference has a matching dependency.
- Every schema input has a valid `modelId`.
- Model inputs, enums, and output paths match fresh OpenAPI evidence.
- Display/final output dependencies are complete.
- The ordered video merge and original-audio merge are explicit.
