# Earthkind

The team's source of truth for Earthkind documents and presentations.

- [Earthkind-Docs.md](Earthkind-Docs.md): document styles, color layers, title rule, named footers, and pagination.
- [Earthkind-Decks.md](Earthkind-Decks.md): slide typography, composition, assets, iconography, and visual checks.
- [Assets](earthkind-deck/assets/): original brand and nature graphics with provenance.
- [Public sample validation](earthkind-deck/validation/report.md): tested scope and known limits.

Always use official Feather utility icons. All linked text is underlined Earthkind olive **#647855**. Preserve link destinations.

See [HANDOFF.md](HANDOFF.md) for copy-and-paste setup and styling prompts.

## Team setup

This repository is public: reading or cloning the brand kit does not require GitHub access approval. Each teammate still needs their own authenticated Google Docs/Slides integration and permission to edit the target file. The kit provides instructions and assets, not account credentials.

```sh
git clone https://github.com/clbowley/Earthkind.git
cd Earthkind
python3 scripts/install.py --agent codex
# Or, for a local Claude skills installation:
python3 scripts/install.py --agent claude
```

The installer creates links to this checkout, not copies of the guides. Keep the checkout in a permanent location. It will not overwrite existing skill folders. Use `--skills-dir /your/skills/folder` for a custom host location. Skill discovery may require reopening the agent session.

The installed skills are `earthkind-docs` and `earthkind-decks`. Invoke the appropriate skill with the artifact URL. The entry point instructs the agent to update a clean main checkout using `git pull --ff-only` before work, then record and hold its VERSION/commit for the job. The host must allow that Git/network operation; this is explicit workflow behavior, not an automatic background subscription.

For browser-only agents, read the current guide and required assets from the public repository using a repository connector or web access. Uploading a ZIP or copying a guide into a project creates a snapshot and will require refreshing it when the source changes.

## Updating the source

1. Edit the two root Markdown files. The files under skill references are links back to them.
2. Update affected recipes or assets, and inspect the relevant example output.
3. Update VERSION and CHANGELOG.md, commit, and push approved changes to main.
4. Other checkouts receive the update on their next successful pull. Existing jobs keep the version they started with.

Use a branch and review for proposed changes. Repository owners should configure team permissions and branch protections to suit their approval process. No collaborators or organization policies are configured by this initial publication.

## Implementation resources

The editable public sample is `earthkind-deck/reference/Earthkind-Sample.pptx`, with slide previews in `reference/render/`. Its five examples use fictional copy, amounts, names, and contact details. Original client documents, exports, portraits, and historical snapshots are excluded from this repository and its history.

`earthkind-deck/reference/recipe.json` and its compiler are synthetic native examples, not a universal converter. IDs beginning `SYNTHETIC_` must never be used for live API requests. Compile a new plan from a fresh target read for actual work; pass live reference IDs in the executor's `protectedPresentationIds` argument. The fourteen semantic archetypes in the guide support different content and structures.

The public validation report covers only synthetic offline fixtures and the new sample previews. It does not certify a new Google Slides run. Every real job still requires native readback and visual inspection.

## Checks

```sh
python3 scripts/install.py --skills-dir /tmp/earthkind-skill-check
node earthkind-deck/scripts/check-adapter.mjs
```

The second check is offline and validates the adapter against the fictional sample geometry. A live document/deck styling task still requires native readback and visual inspection.
