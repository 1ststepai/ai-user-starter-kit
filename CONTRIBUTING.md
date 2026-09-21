# Contributing

Thanks for helping keep this kit useful for people who just started coding with AI.

This repo is **markdown first**. The value is the writing, not a product to install. A small Python script can refresh dated brand examples from our catalog. That is the whole automation.

## What to send

- Typos, broken links, and unclear sentences
- Outdated **tool names** (open an issue if you only spotted it)
- Shorter wording that keeps the same meaning
- Examples a brand-new user can follow without extra tools

Open an issue if you are unsure. Small pull requests are easier to review than large rewrites.

When you change a major guide, bump its **Last reviewed** line and add a bullet to [docs/CHANGELOG.md](docs/CHANGELOG.md).

## Refreshing the tool catalog

Brand examples are not hand-curated in five places. They live in [`data/catalog.json`](data/catalog.json).

1. Edit categories or `examples` there.
2. Bump `version` and `updatedAt` (`YYYY-MM-DD`), and set `asOf` to the month readers should see.
3. Run `python3 scripts/update-kit.py --local` so `docs/starter-map.md` matches.
4. Add a line to `docs/CHANGELOG.md`.

Readers later run `python3 scripts/update-kit.py` (no `--local`) to pull whatever is on `main`. The script only talks to this repo’s GitHub raw URL. Do not add scrapers for vendor docs.

## Voice

Warm, clear, and practical. Short paragraphs. Checklists are fine.

Please do **not**:

- Add consulting, booking, or “hire us” language
- Rank tools as winners or start fanboy wars
- Invent stats, testimonials, or savings claims
- Lead with Auto Model Router or treat it as the product
- Turn CodeFriends into a required step or a paywall
- Add an app, backend, or `npm install` as the core path
- Treat brand lists as forever-accurate

## Docs map

| Page | Job |
| --- | --- |
| [README.md](README.md) | Landing page and value prop |
| [docs/starter-map.md](docs/starter-map.md) | Which *kind* of tool for which job |
| [docs/first-week-playbook.md](docs/first-week-playbook.md) | First-week habits |
| [docs/usage-hygiene.md](docs/usage-hygiene.md) | Cost, secrets, verify-before-push |
| [docs/safety-and-trust.md](docs/safety-and-trust.md) | Drafts, invented answers, review |
| [docs/CHANGELOG.md](docs/CHANGELOG.md) | What’s updated |
| [data/catalog.json](data/catalog.json) | Dated category + example source |
| [scripts/update-kit.py](scripts/update-kit.py) | Pull catalog + refresh the example table |

## Placeholders

Leave these as placeholders unless you have the real value from 1stStep.ai:

- CodeFriends live invite URL (repo link is the stand-in)
- Any extra community URL added later

## License

By contributing, you agree your changes are released under the [MIT License](LICENSE).
