# Keep the starter kit current

Use this when you are in the AI User Starter Kit repo and someone asks which tool to use, or whether the map is up to date.

1. Run `python3 scripts/update-kit.py` (stdlib only). Use `--local` if you must stay offline.
2. Read `data/catalog.json` and the example table in `docs/starter-map.md`.
3. Advise in **categories** (chat / IDE agent / terminal agent / image). Treat brand names as examples as of `asOf`, not a forever list.
4. Do not scrape Cursor, Anthropic, OpenAI, or Google docs. v1 only pulls this repo’s published catalog.
5. If a name looks stale, suggest an issue or PR rather than inventing a new official lineup.

The human guides stay markdown. This skill only refreshes the dated catalog slice.
