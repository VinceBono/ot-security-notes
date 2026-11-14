#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Vince Bono
"""Fail if a relative markdown link points at a file that doesn't exist."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def broken(root: Path) -> list[str]:
    out = []
    for md in sorted(root.rglob("*.md")):
        for target in LINK.findall(md.read_text(encoding="utf-8")):
            path = target.split("#")[0]
            if not path or "://" in target or target.startswith("mailto:"):
                continue
            if not (md.parent / path).exists():
                out.append(f"{md.relative_to(root)}: broken link {target}")
    return out


if __name__ == "__main__":
    errs = broken(Path("."))
    print("\n".join(errs) or "links: ok")
    sys.exit(bool(errs))
