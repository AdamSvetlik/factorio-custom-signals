#!/usr/bin/env python3
"""Build the mod-portal zip for Custom Signals.

Produces custom-signals_<version>.zip in the repo root, containing a single
top-level custom-signals/ folder with only the shipped files (no docs/, .git,
scripts/, tools/, or build artifacts). Version is read from info.json.

Used both locally and by the GitHub Actions release workflow. Pure stdlib so
it runs anywhere Python 3 is available.
"""
import json
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "info.json")) as f:
    version = json.load(f)["version"]

MOD_DIR = "custom-signals"
OUT = os.path.join(ROOT, f"{MOD_DIR}_{version}.zip")

INCLUDE_FILES = ["info.json", "data.lua", "changelog.txt", "thumbnail.png",
                 "README.md", "LICENSE"]
INCLUDE_DIRS = ["prototypes", "graphics", "locale"]


def add(zf, abspath, arcrel):
    zf.write(abspath, os.path.join(MOD_DIR, arcrel))


def main():
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in INCLUDE_FILES:
            p = os.path.join(ROOT, name)
            if os.path.exists(p):
                add(zf, p, name)
        for d in INCLUDE_DIRS:
            base = os.path.join(ROOT, d)
            for dirpath, _, files in os.walk(base):
                for fn in sorted(files):
                    ap = os.path.join(dirpath, fn)
                    rel = os.path.relpath(ap, ROOT)
                    add(zf, ap, rel)
    print(os.path.basename(OUT))


if __name__ == "__main__":
    main()
