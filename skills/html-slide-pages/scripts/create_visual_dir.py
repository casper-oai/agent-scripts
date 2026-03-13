#!/usr/bin/env python3
"""Create a timestamped output folder for HTML visual work.

This helper is intentionally generic. The agent should read the skill's
personal customization notes first, then pass explicit values such as
``--base-dir`` and ``--project-slug`` when local preferences or project
conventions matter.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

DEFAULT_BASE_DIR = Path.home() / "work" / "visuals"
DEFAULT_FALLBACK_PROJECT = "visual_work"


def normalize_slug(value: str) -> str:
    """Convert free-form text into a stable underscore slug for folder names."""
    lowered = value.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "_", lowered)
    lowered = re.sub(r"_+", "_", lowered)
    return lowered.strip("_") or "visual_work"


def infer_project_slug(
    project_slug: str | None,
    hint: str,
    cwd: str,
) -> str:
    """Choose a usable project slug when the agent did not pass one explicitly.

    Preferred behavior:
    - The agent reads personal preferences and supplies ``--project-slug``.
    - If that does not happen, fall back to the working directory name.
    - If the cwd is not helpful, use the hint text.
    - If neither is available, use a generic catch-all slug.
    """
    if project_slug:
        return normalize_slug(project_slug)

    cwd_name = Path(cwd).name.strip()
    if cwd_name:
        return normalize_slug(cwd_name)

    if hint.strip():
        return normalize_slug(hint)

    return DEFAULT_FALLBACK_PROJECT


def build_output_dir(
    *,
    base_dir: Path,
    project_slug: str,
    request_slug: str,
    timestamp: datetime,
) -> Path:
    """Build the final directory path using project, date, and timestamp."""
    day_dir = timestamp.strftime("%Y-%m-%d")
    stamp = timestamp.strftime("%Y%m%d-%H%M%S")
    leaf = f"{stamp}_{normalize_slug(request_slug)}"
    return base_dir / project_slug / day_dir / leaf


def parse_args() -> argparse.Namespace:
    """Read command-line options for the output directory helper."""
    parser = argparse.ArgumentParser(description="Create a timestamped HTML visual output directory.")
    parser.add_argument("--request-slug", required=True, help="Short request label, for example crg_review_heuristics")
    parser.add_argument("--project-slug", help="Optional explicit project slug, for example client_project")
    parser.add_argument("--hint", default="", help="Optional hint for a fallback project slug")
    parser.add_argument("--cwd", default=str(Path.cwd()), help="Working directory related to the request")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR), help="Base visuals directory")
    parser.add_argument("--timestamp", help="Optional timestamp override in YYYYMMDD-HHMMSS format")
    parser.add_argument("--json", action="store_true", help="Print a JSON payload instead of a plain path")
    return parser.parse_args()


def main() -> None:
    """Create the directory, then print the resolved location for downstream use."""
    args = parse_args()
    timestamp = (
        datetime.strptime(args.timestamp, "%Y%m%d-%H%M%S")
        if args.timestamp
        else datetime.now()
    )
    base_dir = Path(args.base_dir).expanduser().resolve()
    project_slug = infer_project_slug(args.project_slug, args.hint, args.cwd)
    output_dir = build_output_dir(
        base_dir=base_dir,
        project_slug=project_slug,
        request_slug=args.request_slug,
        timestamp=timestamp,
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.json:
        print(
            json.dumps(
                {
                    "base_dir": str(base_dir),
                    "project_slug": project_slug,
                    "output_dir": str(output_dir),
                }
            )
        )
        return

    print(str(output_dir))


if __name__ == "__main__":
    main()
