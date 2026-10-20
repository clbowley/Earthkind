---
name: earthkind-docs
description: Apply Earthkind brand styling to documents and Google Docs using the shared Earthkind brand repository. Use when asked to create or restyle an Earthkind document.
---

# Earthkind Docs

This skill is a thin entry point to the shared brand kit. Read `references/Earthkind-Docs.md` in full before styling. Its instructions and companion assets are authoritative; older screenshots cannot override newer explicit rules.

Before a new styling job, resolve this skill directory through symlinks to its Git checkout. If on a clean main branch, run `git pull --ff-only` there to retrieve the approved version. Do not switch branches, reset changes, or silently treat an inaccessible/stale checkout as current. If updating is unavailable, disclose which local version is available. Read VERSION and record the commit used; keep that version fixed until the job is complete.

Use the host's authenticated document tools. Preserve content and link destinations; apply only the requested styling scope. For tables and callouts, use the guide's component treatments and merged-cell handling, then inspect every affected continuation page. Official Feather utility icons and underlined #647855 link text are mandatory. Follow the guide's native editing and visual verification requirements. Report genuine exceptions rather than claiming unverified results.

For compact tables and panel groups, attempt the guide's one-page fit sequence before accepting a split: adjust widths and spacing, permit a controlled margin breakout, and preserve readable type. Verify the complete group in the rendered document.

Apply the guide's universal line-break and pagination check to body text, tables, captions, references, and headings. Resolve runts, widows, and orphans in the rendered output; an API setting alone does not verify the result.

The relative reference links are maintained by the repository. Install by linking this entire skill folder with `scripts/install.py`, not by copying SKILL.md alone. For environments without filesystem/Git access, retrieve the complete current guide and required assets from the public repository using a repository connector or web access.
