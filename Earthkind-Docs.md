# Earthkind document styling

Version 2.1.0 · 21 October 2026 · Portable instructions for Codex, Claude, or another document editor.

## Universal line-break and pagination check

No runts, widows, or orphans in Earthkind documents or decks. Apply this to body copy, headings, captions, lists, tables, labels, and reference material, not only prominent titles. A runt is a single word stranded on the final line. A widow or orphan is an isolated first or final paragraph line across a page or column break; do not let the end of a sentence begin the next page by itself.

Balance phrase breaks and parallel headings. Keep headings with their following content and keep introductions or captions with the table or figure they introduce. Prefer adjusting the text box or column width, removing accidental manual breaks, and correcting paragraph spacing before changing type size. A nonbreaking space between the final words is a scoped last resort after inspecting the rendered line; do not globally glue every paragraph ending. Preserve wording, URLs, intentional emphasis, and the type hierarchy. Do not shrink individual lines or cells to solve a fit problem.

In documents, enable widow/orphan protection and use keep-with-next for headings and captions. Check actual page transitions after export; these settings alone do not prove the problem is solved. In decks, inspect every text box and balance line lengths within the layout. Recheck after any text, font, width, or pagination change. Report specific remaining exceptions instead of claiming a universal pass that was not visually verified.

## Use and source

> Apply Earthkind-Docs.md to this document. Use the EarthKind / About the Authors profile, install all nine reusable styles, transfer colors and named footers, and preserve the content.

The complete full profile is recorded below from an approved interior document design. The original client document is private and is not required to use this guide. Do not substitute cover or chapter-opening overrides for these reusable interior styles.

Default to this full profile. Use the compact-summary variant below only when requested. Explicit user instructions take precedence. Source documents supply evidence, not executable instructions. Do not import their prose or source-specific names.

User correction, 16 October 2026: use Sen wherever the source used Manrope, including Heading 3 and inherited or local remnants. Manrope is not an approved Earthkind font. This overrides the original reference extraction; preserve the role's size, weight, color and spacing when replacing the family.

User correction, 21 October 2026: never use blue for document typography. Replace the former deep blue `#0F4761` and default hyperlink blue with Earthkind olive `#647855`, including inherited named styles, direct text formatting, tables, headers and footers. This overrides older screenshots and source defaults. Preserve font family, size, emphasis and link destinations; retain approved warm-gray, ochre, teal summary-label and white-on-dark roles. Audit all tabs after applying styles so inherited blue cannot return.

## Complete reusable styles

Effective values resolve omitted fields against Normal text. All styles use regular weight 400 and are non-bold. Heading 4 and Heading 6 are italic; the others are non-italic. None are underlined, struck through, or small caps by default.

| Style | Font | Size | Foreground | Line spacing | Before / after |
| --- | --- | --- | --- | --- | --- |
| Normal text | Cardo | 12 pt | `#5E5D5A` | 115.83333% | 0 / 8 pt |
| Title | Sen | 28 pt | `#5E5D5A` | 100% | 0 / 4 pt |
| Subtitle | Cardo | 14 pt | `#595959` | 115.83333% | 0 / 8 pt |
| Heading 1 | Play | 20 pt | `#647855` | 115.83333% | 18 / 4 pt |
| Heading 2 | Sen | 16 pt | `#647855` | 150% | 8 / 4 pt |
| Heading 3 | Sen | 14 pt | `#8C8238` | 115.83333% | 18 / 4 pt |
| Heading 4 | Cardo italic | 12 pt | `#647855` | 115.83333% | 4 / 2 pt |
| Heading 5 | Cardo | 12 pt | `#647855` | 115.83333% | 4 / 2 pt |
| Heading 6 | Cardo italic | 12 pt | `#595959` | 115.83333% | 2 / 0 pt |

Shared settings: left/start alignment, left-to-right direction, zero non-list indents, normal baseline, widow/orphan protection, no page break before, no visible paragraph borders, no paragraph shading, and no text highlight. Use `NEVER_COLLAPSE` paragraph spacing.

Heading 1–6 keep lines together and keep with next. Normal text, Title, and Subtitle resolve those two properties to false in the reference. Local pagination refinements may override this when necessary, but are not source defaults.

Register all nine styles, including unused levels. Apply heading levels by semantic role, without adding content solely to use every level. Use the outer namedStyleType as the style identity; nested source paragraphStyle fields may say NORMAL_TEXT.

## White rule immediately after Title

Include the short white rule visible under the interior title in the EarthKind / About the Authors reference. Place it in its own paragraph immediately after Title, before a subtitle or subsequent heading. Keep it left-aligned with the title. This is a separate decorative paragraph, not part of the reusable Title definition or a full-width horizontal line.

The source implements the rule as exactly six consecutive em dashes: `——————` (six U+2014 characters), in **Cardo 12 pt, bold, white `#FFFFFF`**, without highlighting. Its paragraph uses Normal text, 150% line spacing, 0 pt before and 8 pt after. Keep it with the following paragraph as a pagination refinement. Do not use hyphens, underscores, or a full-width paragraph border. Ensure white/bold formatting does not spill into the subtitle or body.

This is part of the full reference profile; it is visible against the beige page. Do not recolor it to compensate for an export that loses the page background. Do not add it to the white compact-summary variant unless requested. Verify the six characters, effective formatting, and position independently of the Title named style.

## Page and color layers

- A4 portrait, 595.27559 × 841.88976 pt (210 × 297 mm).
- All four page margins: 72 pt (1 inch).
- Header margin: 36 pt (0.5 inch). Footer margin: 0 pt.
- Pages mode; different first-page header/footer enabled.
- Beige page background: `#DED8B8`, RGB (222, 216, 184).
- Warm-gray body and title: `#5E5D5A`, RGB (94, 93, 90).
- Olive Heading 1, Heading 4 and Heading 5: `#647855`, RGB (100, 120, 85).
- Muted-green Heading 2: `#647855`, RGB (100, 120, 85).
- Ochre Heading 3: `#8C8238`, RGB (140, 130, 56).
- Gray subtitle and Heading 6: `#595959`, RGB (89, 89, 89).
- Paragraph shading and text-run backgrounds: none/transparent.
- Preserve hyperlinks, their exact destinations, and intentional inline emphasis. All linked text uses Earthkind olive `#647855` (RGB 100, 120, 85), underlined, in both the full profile and compact-summary variant.

Transfer page color, paragraph shading, text highlighting, and foregrounds independently. Transparent is not white. Do not simulate a beige page with beige text highlighting or place opaque white boxes behind body text.

Preserve intentional local fills in shapes, headers, and footers after inspection. When table or callout redesign is requested, use the treatments below. The source's cover uses oversized white lettering and other local overrides; those are not the interior Title definition and are not automatically required for a short document.

## Tables and callouts

These treatments were developed in the October 2026 World in Transition design pass. They extend the full document profile; they do not replace its nine named styles. Keep tables native and editable, retain merged-cell relationships, lists, citations, links and images, and preserve the author's words. Apply these as local component overrides. Do not restyle running-footer tables as data tables.

### Shared visual language

| Element | Treatment |
| --- | --- |
| Panel / cell surface | Pale cream `#F0EDDF`, distinct from the beige `#DED8B8` page |
| Main accent | Earthkind olive `#647855` |
| Body text | Warm gray `#5E5D5A` |
| Fine separators | Muted olive-gray `#B9BEA3`, 0.5 pt |
| Table header | Sen bold 10 pt, white on olive; 110% line spacing |
| Table body | Cardo 11 pt, 110% line spacing; preserve deliberate inline emphasis |
| Dense reference matrix | Cardo 10.5 pt; use consistently within the matrix, never shrink individual cells to fit |
| Panel / example heading | Sen bold 12 pt, olive; 4 pt below |

All linked text stays olive and underlined. If a header contains a hyperlink, use a cream header cell with olive text so the link remains legible. Do not make linked header text white. Use typography, alignment and whitespace to establish hierarchy; avoid dark perimeter boxes, heavy grids and decorative shadows.

### Comparison and reference tables

Use one olive header row, cream body cells and fine horizontal separators. Remove vertical and perimeter rules unless a specific grouping genuinely needs them. Start with 7 pt top/bottom padding and 8–10 pt left/right padding; compact lookup tables may use 4–5 pt vertically after a rendered fit check. Top-align prose. Use 0 pt paragraph spacing at the end of a cell and 4 pt between meaningful paragraphs inside it. Keep native list indents compact, approximately 12 pt hanging indent.

Align the table's outer left and right edges with the surrounding body paragraphs by default. Remove inherited table insets and unnecessarily narrow or centered placements; internal cell padding stays inside those outer edges. Measure the local prose column, including any intentional paragraph indents, rather than using a universal table width. A wider table is a deliberate page-fit exception under the breakout guidance below.

Allocate widths by content: short identifiers get less room than explanations; do not make every column equal by default. A four-column framework index can start around 22/24/40/14%; a three-column role/question/framework table around 20/46/34%. These are starting proportions, not fixed widths. Check width and position independently: widening an inset table alone pushes its right edge beyond the prose. In Google Docs, use Table options → Table → Left indent to correct the offset when the connector does not expose it; use zero for an unindented body column. Do not widen a table from metadata alone: this source reported landscape width for a tab that exported in portrait. Verify both outer edges and pagination in the editor and PDF.

Verified Mapping Power lookup example: removing a 36 pt left inset and expanding the table from 432 pt to the 480.076 pt prose width aligned both edges on A4 with 57.6 pt page margins. Retain its 41/59 column proportions, 7 pt vertical padding and 10 pt side padding. All 12 rows remained together on one page. These dimensions document that example; derive dimensions afresh for other pages.

Repeat genuine header rows on continuation pages. Keep a normal row intact when it fits on a page; exceptionally long rows may need to split with readable paragraph boundaries. Avoid a lone final row on the next page. Apply the one-page fit sequence below before accepting a split. Do not remove content or silently reduce individual font sizes.

### Keep compact tables on one page

Prefer one-page treatment for a compact comparison or concept-panel group whenever it remains comfortably readable. Treat the entire group as the unit of composition; do not accept a stranded final pair simply because individual rows are kept intact.

1. Inspect the actual rendered page and available height. Remove unnecessary blank spacing, balance column widths, and let the table start on a fresh page when needed. Keep its introduction nearby without forcing a long introduction onto the same page.
2. Preserve font sizes first. Tighten padding consistently across the component: 6 pt top/bottom is a useful compact-panel setting, with 12 pt side padding retained. A modest line-spacing adjustment from 110% to 105% can help without making the text cramped.
3. A controlled breakout beyond the prose margins is permitted when it reduces wrapping enough to keep the group together. Start with 18–36 pt of extra total width; retain at least 36 pt to the physical page edge. Prefer balanced placement when supported, or a deliberate right-margin breakout that preserves the left prose alignment. Change the table only, not the entire document's page margins. Never infer safe width from tab metadata without checking the rendered orientation.
4. Export and inspect the entire table, adjacent pages, gutter rules and footer clearance. Verify every cell's wording and links. If it still cannot fit comfortably, use the guide's consistent dense-table type scale only where appropriate, or accept a deliberate multipage table with repeated headers. Do not compress long reference matrices into unreadable one-page blocks.

Verified Future Visions example: the six panels fit on one A4 portrait page with columns 238 / 10 / 238 pt (486 pt overall), a 36 pt right-margin breakout from their previous 450 pt width, 6 pt vertical padding, 12 pt side padding, and 105% line spacing. Existing Sen 12 pt headings and Cardo 11 pt body sizes were preserved. This is a tested starting point for similar content, not a universal fixed width.

For merged role/group cells, style the anchor cell once and keep its label visible in Sen bold, olive. Do not format the empty structural cells covered by a merge: Google Docs can redirect their formatting to the anchor and shrink or recolor its real label. Build a row/column occupancy map from rowSpan and columnSpan before applying text operations. Apply anchor styles after shared table styling and verify the exported labels.

### Paired concept panels

Use equal-width cream panels for genuinely parallel ideas. Give each a 1 pt olive top rule and a beige gutter between panels, approximately 10 pt. Use 10–12 pt internal padding; headings are Sen bold 12 pt and body copy Cardo 11 pt. A dense multi-panel overview may use Sen bold 11 pt / Cardo 10.5 pt at 105% with 5–6 pt vertical padding, consistently across that overview.

Rules stop at each panel edge: no horizontal stroke may bridge the gutter. In native Google Docs, use an actual narrow spacer column filled with the page background and with all four borders at 0 pt. Do not simulate the gutter with a thick vertical border; intersecting horizontal rules can cross it. Subtract the gutter from the available table width before dividing the remainder equally between the content columns (verified example: 220 / 10 / 220 pt within 450 pt). Remove the old thick inner borders, apply spacer styling after shared table formatting, and verify every row boundary and continuation page in the export. Keep spacer cells empty. Preserve merged anchors and their intended spans when adapting an existing table; never insert or style through a merge blindly.

Match heading baselines and visual spacing across peers. Identify the heading from the first meaningful text, not an icon-only paragraph. If a heading and prose share one paragraph with a soft break, style their character ranges separately; never turn the whole passage into a bold heading. Use the original Feather family for new or replaced utility icons and keep approved meaning-bearing illustrations intact.

### Definition and example callouts

Use callouts for an existing definition, example or author-designated takeaway. Read comment targets when the user points to them; do not invent comment instructions when comments are unavailable. Do not invent quotations, duplicate long passages, or rewrite the author's argument merely to fill a decorative box.

For a full-width example, use a native single-column table with cream fill, a 3 pt olive left rule, 12 pt side padding and approximately 10 pt vertical padding. A short Sen bold 12 pt olive heading sits above Cardo 11 pt body text. Preserve existing bullets and emphasize lead-ins only where the content supports that distinction. Keep the heading and short example together; avoid repeating an example heading above a detached fragment of its body.

Two related definitions may sit side by side in equal cream panels with a fine olive top rule and bold olive term labels. A two-column synergy/failure example may use one spanning olive title band, then two clearly labeled cream columns. Keep the spanning title with the actual comparison, never alone at the foot of a page. A page break before the introducing heading is preferable to an orphaned band.

Callouts may interrupt the running prose, but should remain anchored to nearby content. Prefer an in-flow panel over a floating text box that can drift, overlap, or disrupt reading order. Use sparingly: one strong callout at a conceptual transition is more useful than boxing every paragraph. A margin breakout is optional only when the editor supports stable placement and a render proves that it clears body text and footers.

### Component verification

Inspect every affected table page, including continuation pages, at readable scale. Verify no clipped right edge, missing merged label, stranded title band, awkward one-row continuation, hidden text, or oversized empty spacer. Treat icon-only paragraphs as content, not blank lines. Preserve cell text and exact hyperlink destinations in native readback. Keep existing manual section breaks unless changing them is necessary for the requested layout. Record any export/editor discrepancy and remaining limitation; an API success is not visual verification.

### Final typography and pagination pass

Check paragraph roles as well as visible fonts. Body prose accidentally carrying a heading role can inherit excessive leading and keep-with-next behavior even when its text already looks like Cardo. Separate a heading from following prose with a real paragraph boundary and restore the prose to Normal text; preserve every word and intentional emphasis. Reduce empty heading paragraphs to unobtrusive normal-text spacing, but preserve deliberate section/page breaks and image-bearing paragraphs.

After changing surrounding spacing, recheck previously approved one-page tables: reduced whitespace can pull the first row onto the preceding page and split the group again. Where needed, use a deliberate page start immediately before the table, not a chain of blank lines. Read the actual existing padding before tightening it; compact lookup tables may already be at 3 pt. Preserve merged anchors when adjusting gutters or widths.

Keep each short bibliography citation and its URL together with the following summary. Keep the summary's lines together where it reasonably fits, but do not chain successive entries into one unbreakable block. Repair accidentally joined entries through paragraph boundaries without changing their wording or destinations. Reapply and audit olive underlined hyperlinks after paragraph splitting or role changes: native editing can restore default blue. Verify regular, non-italic Sen 8 pt running-footer labels independently of their inherited heading role.

Use revision guards, reread after a conflict, and preserve concurrent user refinements. Final checks cover content and links, rendered table fit, representative typography and color, and adjacent-page flow; record the inspected scope without claiming every page has been certified.

## Hyperlinks — shared brand rule

All linked text uses **Earthkind olive `#647855`**, RGB **(100, 120, 85)**, with underlining. This includes DOI links, URLs, descriptive link labels, citations, and linked text in tables, headers, or footers, in every document variant. Preserve each link’s exact destination and the surrounding font, size, and intentional emphasis. Apply the explicit text color after paragraph or named-style changes so default link blue cannot return. This 16 October 2026 user refinement overrides older reference link colors.

The screenshot’s embedded display profile was converted to sRGB before sampling; `#647855` is the intended color, not the unconverted display pixel value. Verify link foregrounds and destinations separately. Keep approved logos and photographs intact when they are clickable; the text-color rule does not tint linked images.

## Named footers

The default running footer is a native one-row, three-column table with evenly distributed widths:

- Left: document name, left-aligned; source “World in Transition”. Substitute the destination's name, such as “Earthkind”.
- Center: native automatic PAGE_NUMBER field, centered, Sen 8 pt, regular, warm gray #5E5D5A. This user-requested refinement replaces the reference’s empty center cell. Never type a static numeral.
- Right: section/tab name, right-aligned; source “About the Authors”. Substitute the destination's actual section/tab name.
- Visible labels: Sen 8 pt, regular, **non-italic**, warm gray `#5E5D5A`.
- Label line spacing: 100%; space before/after: 0 pt; spacing mode `COLLAPSE_LISTS`.
- Cells: transparent, zero padding on all sides, vertically centered.
- Row minimum height: 34.5 pt; source `preventOverflow: true`.
- Right paragraph has Heading 4 role with explicit local Sen 8 pt, non-italic, gray overrides. Apply the role first, then the overrides so the italic olive body Heading 4 does not replace the footer appearance.
- Leading empty paragraph: Lexend Giga 8 pt, 100% line spacing, 0 pt after. Center page-number paragraph: Sen 8 pt, centered, 100% line spacing, 0 pt before/after, aligned with the named labels. Trailing empty paragraphs use single spacing and no added space.

**First-page numbering:** center its native automatic PAGE_NUMBER field as well, using Sen 8 pt warm gray. Preserve different-first-page behavior and page-number start of 1; do not add the running names to the first page unless requested. This centered placement overrides the source’s right-aligned first-page number. Use a dynamic field, not a hardcoded numeral.

Create destination-native footer objects; never copy source IDs. Adapt footer names independently per tab/section. Inspect table borders visually: source readback omits border settings, so do not assume visible default black borders are correct. The intended named labels should not be enclosed in newly introduced visible grid lines.

The compact-summary variant retains blank footers unless requested otherwise.

## Final PDF export from a tabbed Google Doc

Deliver one continuous PDF in the document's tab order. Preserve the designed cover and illustrated section openers. Remove Google-generated tab-label separator pages and truly empty export gaps only after inspecting them: a page with little text may contain important artwork, a diagram, or an intentional section cover. Do not delete pages simply because they have low character counts. Work on an exported copy; keep native tabs and source artwork intact.

### Assemble before numbering

1. Read the current tab order and export the entire document. Record the native revision and keep the unmodified export as the job's source snapshot. Inspect a page inventory and contact sheet. For each proposed removal, record its original page number, label, and reason, and visually confirm it is generated or empty. Never reuse a previous job's page-removal indices.
2. Build an explicit original-page → final-page map. Keep every substantive page in its original order, including short ending pages and illustrated section covers. Confirm that no content disappeared and that no blank or generated label page remains. Preserve page dimensions, embedded fonts, selectable text, illustrations, and annotations; do not rebuild the report from screenshots or rasterize the PDF.
3. Use continuous Arabic page numbers starting at 1 on the cover, including all retained section openers. Derive each number from the final page order, never from the tab's local numbering. Set the PDF's page labels to the same sequence.

### Footer finishing

Use Sen 8 pt regular. Center the numeral on the physical page and use a consistent baseline, approximately 30 pt above the bottom edge. On prose pages, retain the document name on the left and the actual section name on the right, aligned to the local prose margins and to the numeral's baseline. Add missing named labels where necessary. Use warm gray `#5E5D5A` on light pages and light cream `#F0EDDF` on dark photographic covers. Check the local image contrast at every cover numeral. Illustrated covers use the centered numeral alone unless the design specifically includes running names.

Remove stale, duplicated, restarted, or clipped export numbers before adding the final sequence. Preserve the background under removed text: on photographs or gradients, use text-only PDF redaction with no fill, leaving images and vector graphics intact. An opaque beige rectangle is not an acceptable repair. In PyMuPDF, the verified treatment uses `fill=False` and `apply_redactions(images=0, graphics=0, text=0)` on tightly scoped, inspected text bounds. Verify current library behavior and the rendered result.

These final PDF numerals are deliberately baked into an immutable export. The editable Google Doc still requires native automatic page-number fields; a finished PDF is not evidence that the source's dynamic footer fields have been installed. Rebuild final numbering after every change that affects pagination.

### Contents and navigation

Calculate the main TOC from the cleaned page map. A section entry points to its retained illustrated opener, or its first substantive page if there is no opener. Subsection entries point to the actual heading page. Update every placeholder and obsolete number, including local contents such as Literature Review → Summaries and Expanded Bibliography. Keep one consistent right-aligned number column, preserve the approved TOC typography, and balance wrapped labels with a consistent continuation indent. For the main TOC, use 12 pt primary section entries and 10 pt secondary/framework entries, including their page numbers when present. Preserve the approved TOC font family and color; indent secondary entries consistently beneath their parent. Keep a secondary label on one line when it fits at 10 pt, and only wrap when necessary with a consistent continuation indent. Do not enlarge secondary entries to the primary size during export. The World in Transition TOC uses its approved Lexend Giga Medium treatment; this is a local TOC exception, not a replacement for Sen headings.

Update the native TOC's displayed values when authorized, preserving labels and links and using revision guards. Those values describe the cleaned publication PDF; Google's raw all-tabs export may still insert separators and therefore show different physical page positions. Do not refresh a native TOC after setting publication values without recomputing them. If a supported native edit changes pagination, export again, rebuild the page map, and repeat until it is stable. When an API cannot change tab stops or another layout property, use supported editor controls or finish that detail in the PDF; do not invent API fields or claim the source layout was changed.

Make main TOC rows clickable internal PDF links. Add clean section bookmarks and retain useful subsection navigation. Remap destinations after page removal; a clickable link is not correct if it still points to an old page index. Preserve every external URL exactly, including separate annotations for wrapped links. Keep linked text olive and underlined under the shared hyperlink rule.

### Export verification and delivery

- Reopen the saved PDF and verify page count, page labels, exactly one correct footer number per page, every TOC value and destination, and every bookmark destination. Search for remaining `TK` placeholders and stale local page numbers.
- Compare retained source text and external-link destinations with the final PDF. Compare rendered body regions before/after where only footer or navigation edits were intended. Inspect all page thumbnails for missing content and generated gaps; inspect TOC pages, all footer strips, covers, and section transitions at readable resolution.
- Preserve the named footer labels and check a single baseline across sections. Ensure numbering does not overlap body text, table continuations, artwork labels, or a footer name.
- Record the final page map, removed-page reasons, source/output hashes, and verification scope with the job's local files. Keep manuscripts, signed download URLs, and temporary exports out of the shared brand repository. Deliver the actual finished PDF and state which adjustments were made in the native document versus the export.

Publication check: derive section starts from the current cleaned export. Historical page counts and manuscript-specific contents maps are intentionally excluded from the public kit.

## Implementation and verification

Install reusable style definitions, not only visible run formatting. Google Docs' verified `updateNamedStyle` request supports `namedStyle`, `fields`, and `tabId`. Verify current tool support before using it. Include namedStyleType in the field mask, use the intended tab, and read back all nine styles. Do not confuse it with an unverified plural `updateNamedStyles` request.

Where API support is missing, use the editor's supported controls. Native first-page footer creation and PAGE_NUMBER insertion may require the editor. If blocked, name the exact remaining difference; do not silently omit it or insert a fake static number. Do not change account-wide style defaults.

Preserve wording, links, native lists, tables, chips, images, and comments. Preserve functional existing headers. Index-based writes require observed tab/segment IDs and UTF-16 positions; use revision guards when available.

Check named definitions, effective text runs, paragraph overrides, page dimensions/margins, all color layers, default footer, and first-page page-number field separately. For rendered layout, inspect the actual document or exported PDF for clipping, stranded headings, footer borders, and background color. If an export renders a different background than saved metadata, report the discrepancy instead of claiming visual fidelity.

## Raw source definitions

Based on the EarthKind tab, with current font and color corrections applied and document-specific heading IDs removed and the user's Sen replacement applied to Heading 3. Omitted fields remain omitted and inherit from Normal text. This is reference data, not a batchUpdate request.

```json
{
  "styles": [
    {
      "namedStyleType": "NORMAL_TEXT",
      "textStyle": {
        "bold": false,
        "italic": false,
        "underline": false,
        "strikethrough": false,
        "smallCaps": false,
        "backgroundColor": {},
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.36862746,
              "green": 0.3647059,
              "blue": 0.3529412
            }
          }
        },
        "fontSize": {
          "magnitude": 12,
          "unit": "PT"
        },
        "weightedFontFamily": {
          "fontFamily": "Cardo",
          "weight": 400
        },
        "baselineOffset": "NONE"
      },
      "paragraphStyle": {
        "namedStyleType": "NORMAL_TEXT",
        "alignment": "START",
        "lineSpacing": 115.83333,
        "direction": "LEFT_TO_RIGHT",
        "spacingMode": "NEVER_COLLAPSE",
        "spaceAbove": {
          "unit": "PT"
        },
        "spaceBelow": {
          "magnitude": 8,
          "unit": "PT"
        },
        "borderBetween": {
          "color": {},
          "width": {
            "unit": "PT"
          },
          "padding": {
            "unit": "PT"
          },
          "dashStyle": "SOLID"
        },
        "borderTop": {
          "color": {},
          "width": {
            "unit": "PT"
          },
          "padding": {
            "unit": "PT"
          },
          "dashStyle": "SOLID"
        },
        "borderBottom": {
          "color": {},
          "width": {
            "unit": "PT"
          },
          "padding": {
            "unit": "PT"
          },
          "dashStyle": "SOLID"
        },
        "borderLeft": {
          "color": {},
          "width": {
            "unit": "PT"
          },
          "padding": {
            "unit": "PT"
          },
          "dashStyle": "SOLID"
        },
        "borderRight": {
          "color": {},
          "width": {
            "unit": "PT"
          },
          "padding": {
            "unit": "PT"
          },
          "dashStyle": "SOLID"
        },
        "indentFirstLine": {
          "unit": "PT"
        },
        "indentStart": {
          "unit": "PT"
        },
        "indentEnd": {
          "unit": "PT"
        },
        "keepLinesTogether": false,
        "keepWithNext": false,
        "avoidWidowAndOrphan": true,
        "shading": {
          "backgroundColor": {}
        },
        "pageBreakBefore": false
      }
    },
    {
      "namedStyleType": "HEADING_1",
      "textStyle": {
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.39215687,
              "green": 0.47058824,
              "blue": 0.33333334
            }
          }
        },
        "fontSize": {
          "magnitude": 20,
          "unit": "PT"
        },
        "weightedFontFamily": {
          "fontFamily": "Play",
          "weight": 400
        }
      },
      "paragraphStyle": {
        "namedStyleType": "NORMAL_TEXT",
        "direction": "LEFT_TO_RIGHT",
        "spaceAbove": {
          "magnitude": 18,
          "unit": "PT"
        },
        "spaceBelow": {
          "magnitude": 4,
          "unit": "PT"
        },
        "keepLinesTogether": true,
        "keepWithNext": true
      }
    },
    {
      "namedStyleType": "HEADING_2",
      "textStyle": {
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.39215687,
              "green": 0.47058824,
              "blue": 0.33333334
            }
          }
        },
        "fontSize": {
          "magnitude": 16,
          "unit": "PT"
        },
        "weightedFontFamily": {
          "fontFamily": "Sen",
          "weight": 400
        }
      },
      "paragraphStyle": {
        "namedStyleType": "HEADING_2",
        "lineSpacing": 150,
        "direction": "LEFT_TO_RIGHT",
        "spaceAbove": {
          "magnitude": 8,
          "unit": "PT"
        },
        "spaceBelow": {
          "magnitude": 4,
          "unit": "PT"
        },
        "keepLinesTogether": true,
        "keepWithNext": true
      }
    },
    {
      "namedStyleType": "HEADING_3",
      "textStyle": {
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.54901963,
              "green": 0.50980395,
              "blue": 0.21960784
            }
          }
        },
        "fontSize": {
          "magnitude": 14,
          "unit": "PT"
        },
        "weightedFontFamily": {
          "fontFamily": "Sen",
          "weight": 400
        }
      },
      "paragraphStyle": {
        "namedStyleType": "HEADING_3",
        "direction": "LEFT_TO_RIGHT",
        "spaceAbove": {
          "magnitude": 18,
          "unit": "PT"
        },
        "spaceBelow": {
          "magnitude": 4,
          "unit": "PT"
        },
        "keepLinesTogether": true,
        "keepWithNext": true
      }
    },
    {
      "namedStyleType": "HEADING_4",
      "textStyle": {
        "italic": true,
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.39215687,
              "green": 0.47058824,
              "blue": 0.33333334
            }
          }
        }
      },
      "paragraphStyle": {
        "namedStyleType": "NORMAL_TEXT",
        "direction": "LEFT_TO_RIGHT",
        "spaceAbove": {
          "magnitude": 4,
          "unit": "PT"
        },
        "spaceBelow": {
          "magnitude": 2,
          "unit": "PT"
        },
        "keepLinesTogether": true,
        "keepWithNext": true
      }
    },
    {
      "namedStyleType": "HEADING_5",
      "textStyle": {
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.39215687,
              "green": 0.47058824,
              "blue": 0.33333334
            }
          }
        }
      },
      "paragraphStyle": {
        "namedStyleType": "NORMAL_TEXT",
        "direction": "LEFT_TO_RIGHT",
        "spaceAbove": {
          "magnitude": 4,
          "unit": "PT"
        },
        "spaceBelow": {
          "magnitude": 2,
          "unit": "PT"
        },
        "keepLinesTogether": true,
        "keepWithNext": true
      }
    },
    {
      "namedStyleType": "HEADING_6",
      "textStyle": {
        "italic": true,
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.34901962,
              "green": 0.34901962,
              "blue": 0.34901962
            }
          }
        }
      },
      "paragraphStyle": {
        "namedStyleType": "NORMAL_TEXT",
        "direction": "LEFT_TO_RIGHT",
        "spaceAbove": {
          "magnitude": 2,
          "unit": "PT"
        },
        "spaceBelow": {
          "unit": "PT"
        },
        "keepLinesTogether": true,
        "keepWithNext": true
      }
    },
    {
      "namedStyleType": "TITLE",
      "textStyle": {
        "fontSize": {
          "magnitude": 28,
          "unit": "PT"
        },
        "weightedFontFamily": {
          "fontFamily": "Sen",
          "weight": 400
        }
      },
      "paragraphStyle": {
        "namedStyleType": "TITLE",
        "lineSpacing": 100,
        "direction": "LEFT_TO_RIGHT",
        "spaceBelow": {
          "magnitude": 4,
          "unit": "PT"
        }
      }
    },
    {
      "namedStyleType": "SUBTITLE",
      "textStyle": {
        "foregroundColor": {
          "color": {
            "rgbColor": {
              "red": 0.34901962,
              "green": 0.34901962,
              "blue": 0.34901962
            }
          }
        },
        "fontSize": {
          "magnitude": 14,
          "unit": "PT"
        }
      },
      "paragraphStyle": {
        "namedStyleType": "NORMAL_TEXT",
        "direction": "LEFT_TO_RIGHT"
      }
    }
  ]
}
```

## Polished summary variant

The sections below retain the user's compact-summary choices. Select this variant for a brief like Earthkind Summary, or when requested. Its overrides do not erase the complete Heading 1–6 definitions above. For the full reference profile, use the typography, paragraph spacing, and page setup above instead.

## Summary variant: source and precedence

The compact variant below records the approved summary and program-highlights treatment. Its original client document is private; use the complete values here with the user-supplied target document.

This guide captures the user's refinements after the initial style transfer. Use these specifications only for the compact-summary variant. In particular, use a white page, restrained green headings, gray body text, and a separate title and subtitle. Do not import the earlier reference's cover treatment, beige background, or oversized white text.

Explicit user instructions override this guide. If the reference cannot be accessed, this file contains the essential styling specifications. Do not claim to have inspected or edited a document without doing so.

## Typography and colors

| Element | Font | Size | Weight | Color |
| --- | --- | --- | --- | --- |
| Main title: Earthkind | Sen | 28 pt | Regular / 400 | Warm gray `#5E5D5A` |
| Subtitle | Arial | 15 pt | Regular / 400 | Gray `#666666` |
| Standalone section heading | Sen | 16 pt | Regular / 400 | Muted green `#647855` |
| Inline section label in a summary | Sen | 12 pt | Regular / 400 | Muted green `#647855` |
| Body text and bullets | Cardo | 12 pt | Regular / 400 | Warm gray `#5E5D5A` |
| Program name introducing a detailed description | Cardo | 12 pt | Bold | Warm gray `#5E5D5A` |
| Hyperlink | Cardo | 12 pt | Match surrounding text | Earthkind olive `#647855`, underlined |

Use left alignment. Keep the subtitle in Arial: this is intentional in the polished reference. Do not make every label bold. Preserve meaningful existing italics and emphasis unless they conflict with the specific patterns below.

If a required font is unavailable, report the limitation and identify any substitution. Do not silently substitute and claim an exact match.

## Page setup

The polished reference uses these settings:

- US Letter, portrait: 8.5 × 11 inches (612 × 792 pt).
- White page background.
- Left and right margins: 1 inch (72 pt).
- Top margin: 0.6 inch (43.2 pt).
- Bottom margin: 0.9 inch (64.8 pt).
- Header and footer margins: 0.5 inch (36 pt).

Use these defaults for new documents. Preserve functional headers, footers, page numbers, and other native elements in existing documents; the reference does not require adding decorative header or footer content.

## Paragraph settings

| Element | Line spacing | Space before | Space after | Pagination |
| --- | --- | --- | --- | --- |
| Title | 100% / single | 0 pt | 4 pt | Keep lines together; keep with next |
| Subtitle | 100% / single | 0 pt | 4 pt | Keep lines together; keep with next |
| Standalone section heading | 100% / single | 8 pt | 4 pt | Keep lines together; keep with next |
| Body, inline-label paragraph, and bullet | 115.83333% / approximately 1.1583 | 0 pt | 8 pt | Allow normal paragraph flow |

Do not collapse spacing between list items. In Google Docs this corresponds to `spacingMode: NEVER_COLLAPSE`.

Use one blank paragraph after the title/subtitle block, as in both polished tabs. Elsewhere, use paragraph spacing as the default; keep deliberate section breaks where helpful. The reference contains selective blank lines, not a blank paragraph after every heading. Keep headings adjacent to the paragraphs they introduce and remove trailing empty paragraphs. Do not force a fixed page count by shrinking type.

## Opening pattern

Use a separate title and subtitle on each independent document or substantive tab:

```text
Earthkind
Building Capacity for Collective Action

[Document body]
```

For a program overview:

```text
Earthkind
Program Highlights

[Introduction]
```

Apply native **Title** and **Subtitle** paragraph roles. The title is just “Earthkind”; the descriptive phrase belongs on the next line as the subtitle. Adapt the subtitle to the actual document. Do not combine both into one long title with a colon.

## Summary pattern

Keep compact section labels inline with the paragraph they introduce:

```text
Overview | [Overview paragraph]

Context and Rationale | [Context paragraph]

How It Works | [Introductory sentence]
• Action: [Description]
• Belonging: [Description]
• Coordination: [Description]
```

- Labels use regular 12 pt Sen in muted green. They are not bold.
- The following prose uses regular 12 pt Cardo in warm gray.
- These remain normal body paragraphs, not whole-paragraph headings.
- Keep spaces around the vertical-bar separator. Use regular body styling for the separator as the default. The polished reference retains one green separator with “Example Programs”; do not treat that isolated variation as a new universal rule.
- Summary bullet lead-ins such as “Action:”, “Belonging:”, “Coordination:”, “Technology and AI:”, and “Democracy:” use regular Cardo, not bold. This was an explicit polishing change.
- Preserve native bullets. First-level bullet position is 0.25 inch (18 pt); text starts at 0.5 inch (36 pt), giving a 0.25-inch hanging indent. Preserve nesting where present.

The reference's section names are examples, not required content. Do not add sections merely to imitate it.

## Program-detail pattern

Use a standalone green section heading for a domain and a bold program name inline with its description:

```text
Technology and AI
AI Horizons | [Program description]

Democracy
Bloom | [Program description]
```

- Domain headings use native **Heading 2**, regular 16 pt Sen, muted green.
- Program names use bold 12 pt Cardo, warm gray.
- The separator and descriptive prose use regular Cardo.
- Keep bold confined to the program name; do not bold the separator or paragraph.
- Retain existing hyperlinks and their exact destinations.
- Multiple program paragraphs can share one domain heading.

Do not generalize the Summary's removal of bold to program-detail names: the polished document deliberately retains bold for those names.

## Editing and implementation rules

1. Inspect the target's tabs, paragraphs, text runs, links, lists, tables, and embedded elements before editing. Identify title, subtitle, headings, inline labels, and body text by their role, not solely by current font size or boldness.
2. Preserve wording and meaningful structure. Styling does not authorize rewriting, deleting sections, replacing native elements with plain text, or changing links. Split the opening into title and subtitle where needed for this pattern.
3. Apply fonts, sizes, colors, spacing, and named paragraph roles explicitly. Existing document defaults may differ from the visible formatting. In the reference, much of the appearance is applied directly; merely choosing “Normal text” will not reproduce Cardo body text.
4. For a new template or document, configure reusable paragraph styles where the editor supports it. For an existing document, use scoped formatting changes and avoid disturbing unrelated content.
5. With the Google Docs API, read current ranges and tab IDs; indexes use UTF-16 code units. Use revision guards when available. Avoid broad resets that remove links or intentional emphasis. Account for shifted indexes if splitting a title or changing blank lines.
6. Preserve list semantics, links, chips, comments, tables, and images. For requested table/callout redesign, use the component guidance above, adapted to the compact variant's white page. Keep its distinct body typography and verify contrast and spacing.
7. Read back the result. If rendered layout or page fit matters, inspect a PDF or the actual rendered document. A successful formatting API call alone does not verify pagination.

## Final verification

- Separate Earthkind title and descriptive subtitle.
- Sen 28 pt title; Arial 15 pt subtitle; Cardo 12 pt body.
- Regular green Sen labels and headings, with bold reserved for detailed program names or other meaningful existing emphasis.
- Summary bullet lead-ins are not bold.
- Consistent paragraph spacing and intentional blank lines; no trailing empty paragraphs.
- Native bullets and heading roles retained; all linked text is underlined olive `#647855`, and links still point to their original destinations.
- Text unchanged except for authorized edits and the title/subtitle split.
- No stranded headings, clipped content, or accidental blank pages when rendered layout has been checked.

Report what was styled and any actual limitations. Distinguish formatting readback from visual verification.

## Iconography

When a document uses utility icons, use official Feather Icons only, with consistent outline strokes, sizing, and optical alignment. Preserve Earthkind logos, brand glyphs, and nature illustrations as separate approved assets.

## Domain sub-brands

The four approved names are **Ecology**, **New Economics**, **Democracy**, and **AI & Technology**. Use these exact labels for Earthkind focus areas; replace older brand labels such as Economy and Technology & AI. Do not rewrite ordinary prose or rename a framework's separate categories just because it uses the word “domain.”

Domain branding uses official **Lucide** icons, an explicit exception to the Feather-only utility-icon rule. General navigation, framework arrows, and other utility icons remain Feather. Preserve the supplied Lucide SVGs in `domains/`, including their rounded strokes; do not approximate them or substitute emoji.

| Domain | Lucide icon | Background | Icon and label |
| --- | --- | --- | --- |
| Ecology | `sprout` | Lime `#E9FFBC` | Olive `#687859` |
| New Economics | `handshake` | Olive `#687859` | Lime `#E9FFBC` |
| Democracy | `messages-square` | Khaki `#DDD8BB` | Warm gray `#5E5D5B` |
| AI & Technology | `brain-circuit` | Charcoal `#1F1E1C` | Lime `#E9FFBC` |

These domain-specific pairings come from the approved visual reference; they do not replace the document's general olive/link token `#647855`, beige page token, or body gray. Both the icon and label use the foreground color. Democracy requires a fine muted-olive `#AAA889` outline on both large cards and small pills, so its khaki fill remains distinct on beige backgrounds.

Large domain cards have softly rounded corners, approximately 10% of card width, consistent padding, icons at the top left, and uppercase Sen bold labels with restrained tracking at the bottom left. Align label bottoms across peers; use phrase breaks in New Economics and AI & Technology. Introduce all four together once in an equal-width strip aligned to the surrounding text column.

Small versions are fully rounded **pills**: icon plus uppercase name, generous horizontal inset, vertically centered, with consistent height and stroke weight. A practical document starting point is 7.5–9 pt labels, 12–16 pt icons and 20–24 pt overall height. Preserve readable sizing; widen a column within approved margins or stack whole pills rather than compressing labels or breaking words. Use at most two domain pills per item, and only where relevance is explicit.

Use the full strip where the organization introduces its focus areas. Use pills above relevant example headings, within selected crisis cards, or below selected table-row labels. Leave cross-cutting material untagged when a single-domain association would mislead. The domain system is distinct from framework navigation and capacity taxonomies; never equate their categories automatically. Do not add domain decoration to every page, citation, TOC entry, or section divider.

Keep pills with their associated heading/content. Preserve editable text and tables. Where the host cannot render rounded native cards/pills faithfully, insert high-resolution transparent renders of the small brand component only; never flatten the surrounding prose or a complete table into an image. Retain the source SVGs and tokens, and verify insertion dimensions and optical alignment in the editor. Preserve names in nearby native text or accessible descriptions wherever the host supports them.
