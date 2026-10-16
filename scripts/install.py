#!/usr/bin/env python3
"""Link the canonical repo skills into a local agent installation; never overwrite."""
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--agent', choices=['codex', 'claude'], default='codex')
parser.add_argument('--skills-dir', type=Path, help='Override the destination skills directory')
args = parser.parse_args()
repo = Path(__file__).resolve().parents[1]
default = (Path(os.environ.get('CODEX_HOME', Path.home()/'.codex'))/'skills'
           if args.agent == 'codex' else Path.home()/'.claude'/'skills')
destination = (args.skills_dir or default).expanduser().absolute()
sources = [repo/'skills'/'earthkind-docs', repo/'skills'/'earthkind-decks']

# Preflight all entries before writing any, so a conflict cannot partially install.
for source in sources:
    target = destination/source.name
    if target.exists() or target.is_symlink():
        if not target.is_symlink() or target.resolve() != source:
            parser.error(f'Refusing to overwrite {target}. Choose another --skills-dir or reconcile it explicitly.')
    if not (source/'SKILL.md').is_file():
        parser.error(f'Missing skill: {source}')
destination.mkdir(parents=True, exist_ok=True)
for source in sources:
    target = destination/source.name
    if not target.is_symlink():
        target.symlink_to(source, target_is_directory=True)
    guide = next((target/'references').glob('Earthkind-*.md'))
    if not guide.is_file():
        raise RuntimeError(f'Broken canonical guide link: {guide}')
    print(f'{target} -> {source}')
