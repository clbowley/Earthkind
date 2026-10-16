# Public sample validation

16 October 2026 · Kit 2.0.0

The five-slide public sample was created from fictional copy, names, contact details, and financial figures. Its source is `reference/sample-layout.json`; the editable PPTX and five previews are in `reference/`. Original client decks, photos, speaker notes, exports, native IDs, and validation snapshots are not included.

## Checked in this release

- PPTX structure, encoded Sen/Inter fonts, heading fit, and first-party Artifact Tool import pass.
- All five previews were rendered with locally registered Sen and Inter fonts and inspected at 1280 × 720.
- The three intentional artwork bleeds on slides 2, 4, and 5 match the guide; these are not content overflow.
- The provider-neutral adapter reproduces 55 synthetic expected element geometries exactly in an offline mock.
- The executor rejects a synthetic target outside the offline fixture and rejects explicitly protected reference IDs.
- Both skills install as links to the canonical guides.
- Only fictional example contact information is included. Embedded PPTX XML, notes, and relationships are included in the publication audit.

## Limits

The examples illustrate selected compositions; they are not a complete fourteen-slide template. The public recipe has synthetic object IDs and cannot be applied directly to a live deck. Adapt from a fresh authorized target read, preserve its content, and render the actual output. The sample has not been rendered in native PowerPoint or Google Slides. Historical client validation does not certify this public sample or future jobs.

## Rebuild offline fixtures

Run `python3 earthkind-deck/scripts/build-sample-fixtures.py`, then `node earthkind-deck/scripts/check-adapter.mjs`. This regenerates synthetic JSON and request fixtures, not the PPTX or slide previews. If the sample composition changes, update and inspect the editable PPTX and previews too.
