---
name: earthkind-decks
description: Apply Earthkind brand styling to presentations and Google Slides using the shared Earthkind brand repository. Use when asked to create or restyle an Earthkind deck.
---

# Earthkind Decks

This skill is a thin entry point to the shared brand kit. Read `references/Earthkind-Decks.md` in full before styling. Its instructions and companion assets are authoritative; older screenshots cannot override newer explicit rules.

Before a new styling job, resolve this skill directory through symlinks to its Git checkout. If on a clean main branch, run `git pull --ff-only` there to retrieve the approved version. Do not switch branches, reset changes, or silently treat an inaccessible/stale checkout as current. If updating is unavailable, disclose which local version is available. Read VERSION and record the commit used; keep that version fixed until the job is complete.

Use the host's authenticated document tools. Preserve content and link destinations; apply only the requested styling scope. Official Feather utility icons and underlined #647855 link text are mandatory. Use the four approved Lucide domain marks, colors, rounded cards, and outlined Democracy pills exactly as specified in the Domain sub-brands section; this is the explicit exception to the utility-icon rule. Follow the guide's native editing and visual verification requirements. Report genuine exceptions rather than claiming unverified results.

Apply the guide's universal line-break and pagination check to all slide text, including tables, captions, and notes. Balance lines and resolve isolated final words in the rendered slides; do not treat a font-size or line-height setting as proof of fit.

The relative reference links are maintained by the repository. Install by linking this entire skill folder with `scripts/install.py`, not by copying SKILL.md alone. For environments without filesystem/Git access, retrieve the complete current guide and required assets from the public repository using a repository connector or web access.
