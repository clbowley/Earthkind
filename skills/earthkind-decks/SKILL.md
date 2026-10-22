---
name: earthkind-decks
description: Apply Earthkind brand styling to presentations and Google Slides using the shared Earthkind brand repository. Use when asked to create or restyle an Earthkind deck.
---

# Earthkind Decks

This skill is a thin entry point to the shared brand kit. Read `references/Earthkind-Decks.md` in full before styling. Its instructions and companion assets are authoritative; older screenshots cannot override newer explicit rules.

Before a new styling job, resolve this skill directory through symlinks to its Git checkout. If on a clean main branch, run `git pull --ff-only` there to retrieve the approved version. Do not switch branches, reset changes, or silently treat an inaccessible/stale checkout as current. If updating is unavailable, disclose which local version is available. Read VERSION and record the commit used; keep that version fixed until the job is complete.

Use the host's authenticated document tools. Preserve content and link destinations; apply only the requested styling scope. Official Feather utility icons and underlined #647855 link text are mandatory. Use the four approved Lucide domain marks, colors, rounded cards, and outlined Democracy pills exactly as specified in the Domain sub-brands section; this is the explicit exception to the utility-icon rule. Follow the guide's native editing and visual verification requirements. Report genuine exceptions rather than claiming unverified results.

Apply the guide's universal line-break and pagination check to all slide text, including tables, captions, and notes. Balance entire phrases, including introductory body copy above cards, and resolve isolated final words or disproportionately short final lines in the rendered slides. Use soft breaks within a paragraph so line balancing does not add paragraph spacing; do not treat a font-size or line-height setting as proof of fit.

The relative reference links are maintained by the repository. Install by linking this entire skill folder with `scripts/install.py`, not by copying SKILL.md alone. For environments without filesystem/Git access, retrieve the complete current guide and required assets from the public repository using a repository connector or web access.

Remove slide numbers by default. Apply the current corner-logo, translucent-panel, connected-pillar and portrait rules; compile comment implementation status privately. Do not publish client comments or assets in this public repository. Use current guide rules over historical visual fixtures.

Use the shared translucent panel system: cream at 25% opacity, one 2 pt top or left accent, and foreground colors chosen for the composed background. Strongly rounded domain identity cards retain their colors at 85% opacity without highlight strokes. Preserve photo coverage through the full oval, not just its center.

Progress and companion examples use the Funding-pair large green glyph treatment behind three translucent column windows and the shared backbone.
