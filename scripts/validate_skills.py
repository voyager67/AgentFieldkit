#!/usr/bin/env python3
"""Validate AgentFieldkit Agent Skills using only the Python standard library."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, "missing or malformed YAML frontmatter"
    fields = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            return None, f"invalid frontmatter line: {raw_line!r}"
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in fields:
            return None, f"duplicate frontmatter key: {key}"
        fields[key] = value.strip('"\'')
    return fields, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    args = parser.parse_args()
    skill_root = args.root.resolve() / "skills"
    if not skill_root.is_dir():
        print(f"ERROR: skills directory not found: {skill_root}", file=sys.stderr)
        return 2
    directories = sorted(p for p in skill_root.iterdir() if p.is_dir())
    if not directories:
        print("ERROR: no skill folders found", file=sys.stderr)
        return 2
    errors = []
    seen = set()
    for directory in directories:
        manifest = directory / "SKILL.md"
        rel = manifest.relative_to(args.root.resolve())
        if not NAME_RE.fullmatch(directory.name):
            errors.append(f"{rel}: directory name must be lowercase letters/digits/hyphens")
        if not manifest.is_file():
            errors.append(f"{rel}: SKILL.md is missing")
            continue
        text = manifest.read_text(encoding="utf-8")
        fields, error = parse_frontmatter(text)
        if error:
            errors.append(f"{rel}: {error}")
            continue
        name, description = fields.get("name", ""), fields.get("description", "")
        if not name:
            errors.append(f"{rel}: name is required")
        elif not NAME_RE.fullmatch(name):
            errors.append(f"{rel}: name must be lowercase letters/digits/hyphens")
        elif name != directory.name:
            errors.append(f"{rel}: name {name!r} does not match folder {directory.name!r}")
        if name in seen:
            errors.append(f"{rel}: duplicate name {name!r}")
        seen.add(name)
        if not description:
            errors.append(f"{rel}: description is required")
        elif len(description) > 1024:
            errors.append(f"{rel}: description exceeds 1024 characters")
        if len(name) > 64:
            errors.append(f"{rel}: name exceeds 64 characters")
        body = text[FRONTMATTER_RE.match(text).end():] if FRONTMATTER_RE.match(text) else ""
        if not body.strip():
            errors.append(f"{rel}: skill instructions are empty")
        if len(text.splitlines()) < 12:
            errors.append(f"{rel}: skill is suspiciously short; add procedure and boundaries")
    if errors:
        print(f"Validation failed: {len(errors)} issue(s)")
        for item in errors:
            print(f"- {item}")
        return 1
    print(f"Validated {len(directories)} skills: metadata, folder names, and instruction bodies look good.")
    print("Note: this lightweight checker validates common metadata rules; it is not a full YAML parser or host-specific compatibility test.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
