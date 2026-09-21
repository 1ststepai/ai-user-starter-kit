# AI User Starter Kit

A free first-week guide for people who just started coding with AI.

Pick one tool. Ship one small project. Learn the habits that keep you safe and in control.

No signup. No sales call. Read it in a sitting, use it for a week.

Built by [1stStep.ai](https://1ststep.ai).

## What’s inside

Four short pages. Read them in order, or jump to the one you need.

1. **[Starter map](docs/starter-map.md)** — chat vs IDE agent vs terminal agent vs image. Categories first; brand names are examples as of a month.
2. **[First-week playbook](docs/first-week-playbook.md)** — one small project, better prompts, when to read the diff, when to restart the chat.
3. **[Usage hygiene](docs/usage-hygiene.md)** — tokens and cost without the scare story; secrets; production; verify before you commit.
4. **[Safety and trust](docs/safety-and-trust.md)** — models invent things; never paste API keys; review changes; treat output as a draft.

You do not need prior jargon. Where we use a term (`diff`, `agent`, `tokens`), the page defines it once.

## Living kit

The guides stay readable markdown. The **tool map** updates itself from a published catalog — not a PDF you wait on, and not a changelog you have to remember.

Categories and dated brand examples live in [`data/catalog.json`](data/catalog.json). When that file changes on `main`, one command (below) pulls it onto your clone and refreshes the starter map.

Each major guide also shows a **Last reviewed** date. If a name looks wrong, [open an issue](https://github.com/1ststepai/ai-user-starter-kit/issues) or a small PR.

## Keep it current

```bash
python3 scripts/update-kit.py
```

Python 3 only. No packages. No account.

That fetches this repo’s catalog from GitHub raw (`main`), overwrites local `data/catalog.json` if remote `version` / `updatedAt` is newer, rewrites the example table in the starter map, and prints what changed. It will not call any other host.

You will know it worked when the command prints the remote version and either `Updated data/catalog.json` or `No newer catalog; keeping local`.

**Publish path for 1stStep:** when tools or models change, edit `data/catalog.json` on `main`, bump `version` and `updatedAt`, run `python3 scripts/update-kit.py --local`, add a line to [docs/CHANGELOG.md](docs/CHANGELOG.md). Everyone who runs the command later gets the new map. That is the automatic loop. Future: richer sources. v1 does not scrape vendor docs.

A lightweight reminder for agents lives in [`skills/keep-kit-current/SKILL.md`](skills/keep-kit-current/SKILL.md).

## Who this is for

You installed a chat, an IDE agent, a terminal agent, or something like them, and you want a calm first week — not a feed of “must-use” extensions.

This kit is not a product pitch, a course, or a reason to hire anyone. It is a map and a practice loop.

## How to start (10 minutes)

1. Open the [starter map](docs/starter-map.md) and choose **one** tool you already have.
2. Create a throwaway folder. Tell the AI that folder is the only place it may edit.
3. Follow [day 1](docs/first-week-playbook.md) — a “hello” you can open without the AI.
4. Keep [hygiene](docs/usage-hygiene.md) and [safety](docs/safety-and-trust.md) nearby when you touch keys or git.

Later, when the industry moves: `python3 scripts/update-kit.py` — you do not need a new download of the whole kit.

## What’s updated

Latest: **1.0.0** (21 September 2026) — first public kit + catalog v1.

Full list: [docs/CHANGELOG.md](docs/CHANGELOG.md).

## GitHub Pages

This repo is ready to publish as static docs.

In the repository **Settings → Pages**, set **Source** to **Deploy from a branch**, branch `main` (or this release branch), folder **`/docs`**. GitHub will build the Markdown with the Cayman theme already listed in [`docs/_config.yml`](docs/_config.yml).

A tiny HTML mirror of this README lives at [`index.html`](index.html) if you later serve the repo root instead.

## License

[MIT](LICENSE). Use it, copy it, and share it.

Fixes and clarifications are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

### Optional: CodeFriends

If you want company while you learn — not a class, not a paywall — [CodeFriends](https://github.com/1ststepai/codefriends) is a small, optional community for people figuring this out together.

What people ask there is the feedback loop that keeps this kit honest: questions in → catalog and guides update. You do not need to join to use the kit.

The live invite URL may be added later. Until then, that repo is the placeholder.

1stStep.ai builds this kit and hosts the community invite.

---

### Optional: Auto Model Router

Skip this until week one is done.

If you later start optimizing spend across IDE agents, terminal agents, and similar tools, [Auto Model Router](https://github.com/1ststepai/auto-model-router) is an open, confirm-before-run routing skill. It does not replace Cursor Auto, and we do not claim it beats any vendor picker.
