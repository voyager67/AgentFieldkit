#!/usr/bin/env python3
"""Install AgentFieldkit skills to a documented coding-agent skills directory."""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"


def target_path(agent: str, scope: str, project_root: Path, home: Path) -> Path:
    if scope == "project":
        mapping = {
            "claude": ".claude/skills",
            "codex": ".agents/skills",
            "cursor": ".agents/skills",
            "gemini": ".agents/skills",
            "copilot": ".github/skills",
            "generic": ".agents/skills",
        }
        return project_root / mapping[agent]
    mapping = {
        "claude": ".claude/skills",
        "codex": ".agents/skills",
        "cursor": ".agents/skills",
        "gemini": ".agents/skills",
        "copilot": ".copilot/skills",
        "generic": ".agents/skills",
    }
    return home / mapping[agent]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=["claude", "codex", "cursor", "gemini", "copilot", "generic"], required=True)
    parser.add_argument("--scope", choices=["user", "project"], default="user")
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--destination", type=Path, help="Override destination directory")
    parser.add_argument("--skill", help="Install one named skill; defaults to all")
    parser.add_argument("--overwrite", action="store_true", help="Replace destination skill directories (can discard local edits)")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without copying")
    args = parser.parse_args()

    if args.destination:
        dest_root = args.destination.expanduser().resolve()
    else:
        dest_root = target_path(args.agent, args.scope, args.project_root.expanduser().resolve(), Path.home())
    available = {p.name: p for p in SKILLS_ROOT.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    if args.skill:
        if args.skill not in available:
            print(f"ERROR: unknown skill {args.skill!r}. Run with --help or inspect skills/.", file=sys.stderr)
            return 2
        selected = [available[args.skill]]
    else:
        selected = sorted(available.values())
    if not selected:
        print("ERROR: no skills found", file=sys.stderr)
        return 2

    # Guard against an override that would target the canonical source library.
    try:
        dest_root.relative_to(SKILLS_ROOT.resolve())
    except ValueError:
        pass
    else:
        print(f"ERROR: destination cannot be inside the canonical skills source: {dest_root}", file=sys.stderr)
        return 2

    print(f"Target: {dest_root}")
    installed = skipped = 0
    for source in selected:
        target = dest_root / source.name
        if target.exists() and not args.overwrite:
            print(f"SKIP  {source.name}: destination exists (use --overwrite only if replacing local edits is intended)")
            skipped += 1
            continue
        print(f"{'PLAN ' if args.dry_run else 'COPY '} {source.name} -> {target}")
        if not args.dry_run:
            dest_root.mkdir(parents=True, exist_ok=True)
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(source, target)
        installed += 1
    action = "planned" if args.dry_run else "installed"
    print(f"Done: {installed} {action}, {skipped} skipped.")
    if args.agent == "generic":
        print("Confirm that the selected host discovers skills from this destination.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
