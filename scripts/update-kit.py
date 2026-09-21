#!/usr/bin/env python3
"""Refresh this kit from the published 1stStep catalog.

Default: fetch data/catalog.json from this repo's main branch (GitHub raw only),
keep it if newer, then rewrite the dated example table in docs/starter-map.md.

No extra packages. No secrets. No vendor-doc scraping.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"
STARTER_MAP = ROOT / "docs" / "starter-map.md"
DEFAULT_URL = (
    "https://raw.githubusercontent.com/1ststepai/ai-user-starter-kit/main/data/catalog.json"
)
ALLOWED_PREFIX = "https://raw.githubusercontent.com/1ststepai/ai-user-starter-kit/"
EXAMPLES_START = "<!-- catalog:examples:start -->"
EXAMPLES_END = "<!-- catalog:examples:end -->"
REVIEWED_START = "<!-- catalog:reviewed:start -->"
REVIEWED_END = "<!-- catalog:reviewed:end -->"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_version(raw: str) -> tuple[int, ...]:
    parts = []
    for piece in str(raw).split("."):
        digits = "".join(ch for ch in piece if ch.isdigit())
        parts.append(int(digits) if digits else 0)
    return tuple(parts) or (0,)


def parse_day(raw: str) -> date:
    return date.fromisoformat(str(raw)[:10])


def is_newer(remote: dict, local: dict) -> bool:
    remote_day = parse_day(remote["updatedAt"])
    local_day = parse_day(local["updatedAt"])
    if remote_day != local_day:
        return remote_day > local_day
    return parse_version(remote["version"]) > parse_version(local["version"])


def validate(catalog: dict) -> None:
    for key in ("version", "updatedAt", "asOf", "categories"):
        if key not in catalog:
            raise ValueError(f"catalog missing {key}")
    parse_day(catalog["updatedAt"])
    parse_version(catalog["version"])
    if not isinstance(catalog["categories"], list) or not catalog["categories"]:
        raise ValueError("catalog.categories must be a non-empty list")
    for row in catalog["categories"]:
        for key in ("id", "name", "examples"):
            if key not in row:
                raise ValueError(f"category missing {key}")


def fetch_catalog(url: str) -> dict:
    if not url.startswith(ALLOWED_PREFIX):
        raise ValueError(
            f"refusing URL (only {ALLOWED_PREFIX}… is allowed): {url}"
        )
    req = urllib.request.Request(url, headers={"User-Agent": "ai-user-starter-kit-update/1"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        payload = resp.read().decode("utf-8")
    catalog = json.loads(payload)
    validate(catalog)
    return catalog


def render_examples(catalog: dict) -> str:
    as_of = catalog["asOf"]
    lines = [
        f"_Examples as of {as_of}._ Names change; the categories above do not.",
        "",
        "| Category | Examples |",
        "| --- | --- |",
    ]
    for row in catalog["categories"]:
        examples = ", ".join(row["examples"])
        lines.append(f"| {row['name']} | {examples} |")
    return "\n".join(lines) + "\n"


def render_reviewed(catalog: dict) -> str:
    return (
        f"_Last reviewed: {catalog['asOf']}. "
        "Brand names below are examples, not a forever list._\n"
    )


def replace_block(text: str, start: str, end: str, body: str) -> str:
    if start not in text or end not in text:
        raise ValueError(f"missing markers {start} … {end} in {STARTER_MAP.name}")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return f"{before}{start}\n{body}{end}{after}"


def write_starter_map(catalog: dict) -> bool:
    original = STARTER_MAP.read_text(encoding="utf-8")
    updated = replace_block(original, EXAMPLES_START, EXAMPLES_END, render_examples(catalog))
    updated = replace_block(updated, REVIEWED_START, REVIEWED_END, render_reviewed(catalog))
    if updated == original:
        return False
    STARTER_MAP.write_text(updated, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--local",
        action="store_true",
        help="do not fetch; refresh markdown from the catalog already on disk",
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help="GitHub raw URL for this repo's catalog (default: main)",
    )
    args = parser.parse_args(argv)

    local = load_json(CATALOG_PATH)
    validate(local)
    print(f"Local catalog: {local['version']} ({local['updatedAt']}, {local['asOf']})")

    catalog = local
    if args.local:
        print("Skipping fetch (--local).")
    else:
        try:
            remote = fetch_catalog(args.url)
        except urllib.error.HTTPError as exc:
            print(f"Remote catalog not available ({exc.code} from {args.url}). Keeping local.")
        except urllib.error.URLError as exc:
            print(f"Could not reach catalog ({exc.reason}). Keeping local.")
        except (ValueError, json.JSONDecodeError) as exc:
            print(f"Remote catalog rejected ({exc}). Keeping local.")
        else:
            print(f"Remote catalog: {remote['version']} ({remote['updatedAt']}, {remote['asOf']})")
            if is_newer(remote, local):
                CATALOG_PATH.write_text(
                    json.dumps(remote, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
                catalog = remote
                print(f"Updated {CATALOG_PATH.relative_to(ROOT)}")
            else:
                print("No newer catalog; keeping local.")

    changed = write_starter_map(catalog)
    rel = STARTER_MAP.relative_to(ROOT)
    if changed:
        print(f"Refreshed {rel} example table (as of {catalog['asOf']}).")
    else:
        print(f"{rel} already matched the catalog.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
