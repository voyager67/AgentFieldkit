#!/usr/bin/env python3
"""Create standalone skill ZIPs for ChatGPT Skills or Claude web custom Skills."""
from __future__ import annotations
import argparse
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=["chatgpt", "claude"], default="chatgpt", help="Target skill-upload interface")
    parser.add_argument("--output", type=Path, help="Output directory; defaults to dist/<target>")
    parser.add_argument("--skill", help="Package one named skill; defaults to all")
    args = parser.parse_args()
    skills_root = ROOT / "skills"
    skills = sorted(p for p in skills_root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if args.skill:
        skills = [p for p in skills if p.name == args.skill]
        if not skills:
            parser.error(f"unknown skill: {args.skill}")
    output_path = args.output if args.output is not None else ROOT / "dist" / args.target
    out = output_path.expanduser().resolve()
    try:
        out.relative_to(skills_root.resolve())
    except ValueError:
        pass
    else:
        parser.error("output directory cannot be inside the canonical skills source")
    out.mkdir(parents=True, exist_ok=True)
    count = 0
    for skill in skills:
        archive = out / f"{skill.name}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(skill.rglob("*")):
                if path.is_file():
                    zf.write(path, arcname=(Path(skill.name) / path.relative_to(skill)).as_posix())
        print(f"Created {archive}")
        count += 1
    ui = "ChatGPT desktop Skills" if args.target == "chatgpt" else "Claude custom Skills"
    print(f"Packaged {count} skill(s) for {ui}. Upload each ZIP through that product's Skills interface.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
