# Earthkind agent setup

Source of truth: https://github.com/clbowley/Earthkind

- [Document guide](Earthkind-Docs.md)
- [Presentation guide](Earthkind-Decks.md)
- [Editable fictional sample](earthkind-deck/reference/Earthkind-Sample.pptx)

Reading this public kit does not require a GitHub invitation. Editing a Google Doc or Slides deck requires your own connected Google account and access to that file. The kit includes instructions and assets, not account credentials. Keep client documents and generated outputs outside this public repository.

## First-time setup prompt

```text
Set up the Earthkind brand kit from https://github.com/clbowley/Earthkind.git using main.

Read README.md. Clone into a permanent local folder, or inspect an existing checkout without discarding local changes. Install both skills using python3 scripts/install.py --agent codex or --agent claude, as appropriate for this environment. Preserve existing skill folders if there is a conflict.

Verify that earthkind-docs and earthkind-decks resolve to the canonical guides and assets. Report VERSION, commit, and whether the session needs reopening. Check my Google Docs/Slides editing connection and explain any missing access.

Before each new job, update a clean main checkout with git pull --ff-only. Record and keep that version fixed for the job. If filesystem installation is unavailable, read the complete current guides and assets from the public repository using supported web or repository tools; explain that limitation.
```

## Document prompt

```text
Use earthkind-docs on [GOOGLE DOC LINK]. Preserve content and link destinations. Apply the complete guide, including typography, colors, tables, spacing, title rules, and named footers. Inspect the rendered pages and repair awkward breaks, overflow, and inconsistencies.

Also produce a clean PDF using the export workflow: integrate tabs, remove only generated separator or empty pages, preserve intentional covers, add continuous centered page numbers, and update the TOC from the final page map. Report the version used, what was verified, and any limitations.
```

## Presentation prompt

```text
Use earthkind-decks on [GOOGLE SLIDES LINK]. Preserve content and link destinations. Apply the approved typography, colors, layouts, original brand assets, and Feather icons. Balance line breaks, standardize spacing, and keep decorative artwork behind content.

Inspect every rendered slide and repair overflow, alignment, contrast, and spacing issues. Report the guide version, what was verified, and any limitations. Public sample names and financial figures are fictional; never insert them into my content.
```
