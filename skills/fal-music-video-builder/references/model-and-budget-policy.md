# Model and Budget Policy

Model catalogs, prices, and parameter ranges drift. Use live official fal model pages and OpenAPI schemas on every build; record the access timestamp and direct source URL in the schema catalog.

## Selection

1. Translate the creative brief into requirements: reference-image support, first/last frame, character consistency, resolution, aspect ratio, motion complexity, acceptable duration granularity, and total generated seconds.
2. Shortlist current image and image-to-video endpoints that satisfy those requirements.
3. Calculate image calls, edit/variation calls, total video seconds, utility calls, and likely retries using current prices.
4. Hold back 15–20% for retries. Planned first-pass spend should ordinarily stay at or below 80–85% of the hard budget.
5. If no plan fits, offer explicit scope/resolution/model tradeoffs. Never silently exceed budget or omit sections.

## Timing

Keep full decimal audio duration. Use only durations accepted by the chosen live schema. Prove:

`song_duration + 2 <= sum(clip durations) <= song_duration + 5`

Target +3 seconds and round upward to a frame boundary. If a discrete-duration model cannot solve the final interval, choose a finer-grained model for the final clip or a currently verified padding/composition endpoint. Never trim the visual timeline below the song.

Do not assume audio/video merge behavior for unequal durations. Record `final_duration_strategy_verified: true` only after official schema/documentation or a non-paid dry validation establishes the behavior. Native model audio should be false unless approved for a specific creative use.

## Starting research points

- [fal image-to-video comparison](https://fal.ai/explore/image-to-video-apis)
- [Wan 2.7 image-to-video](https://fal.ai/models/fal-ai/wan/v2.7/image-to-video/api)
- [Kling 3 Pro image-to-video](https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video)
- [Seedance 1.5 Pro image-to-video](https://fal.ai/models/fal-ai/bytedance/seedance/v1.5/pro/image-to-video)
- [Wan 2.2 A14B image-to-video](https://fal.ai/models/fal-ai/wan/v2.2-a14b/image-to-video)
- [FLUX Schnell](https://fal.ai/models/fal-ai/flux/schnell)
- [FLUX 2 Pro](https://fal.ai/models/fal-ai/flux-2-pro)
- [Nano Banana Pro](https://fal.ai/nano-banana-pro)
- [Merge videos](https://fal.ai/models/fal-ai/ffmpeg-api/merge-videos/api)
- [Merge audio/video](https://fal.ai/models/fal-ai/ffmpeg-api/merge-audio-video/api)

These are discovery candidates, not defaults. Live schema and price evidence controls.

## Schema catalog record

For each exact app ID record `source_url`, `verified_at`, `allowed_inputs`, `required_inputs`, `allowed_values`, `output_paths`, `rate_usd_per_call`, and `rate_usd_per_second`. Use zero only when the official price is genuinely free, not when it is unknown. Each planned clip must include `id`, `model_app`, positive `start_seconds`, positive `duration_seconds`, `continuity_ids`, and `generate_audio: false`. The plan also records `aspect_ratio`, `final_duration_evidence_url`, and the exact original-audio merge strategy.
