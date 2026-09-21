---
title: Starter map
---

# Starter map

<!-- catalog:reviewed:start -->
_Last reviewed: September 2026. Brand names below are examples, not a forever list._
<!-- catalog:reviewed:end -->

You do not need every AI tool. You need one that matches the **job** in front of you.

**Pick one primary tool and learn it for a week.** Switching apps every day feels productive and usually isn't.

There is no best brand here. Names change. The useful split is *what the tool can see and change* — a **category**, not a logo.

## The four jobs

### 1. Chat — think and draft

A browser (or app) conversation. You copy and paste.

**Good for:** explaining an idea, outlining a plan, rewriting a paragraph, asking “what does this error mean?”, and practicing prompts.

**Not good for:** editing the files in your real project by itself. That is fine in week one.

Use chat when you want a conversation, not a roommate in your codebase.

### 2. IDE agent — edit the project in front of you

An editor with an agent that can change files and show a *diff* (the list of proposed edits).

**Good for:** working in the same window as your code and seeing each edit.

**Not good for:** blindly accepting a huge rewrite you have not read.

If you already open a code editor to work, an IDE agent is the most natural next step.

### 3. Terminal agent — run commands where you already work

An agent you drive from a command line. It can inspect files, run tests, and propose git commands.

**Good for:** people who already live in a terminal.

**Not good for:** week one if the terminal still feels like a dark room. You can come back to this.

A terminal agent can do more than chat — including things that are hard to undo. Stay on a practice folder until you trust the loop.

### 4. Image — pictures, not programs

A picture generator. Optional. Not a substitute for the three jobs above.

**Good for:** a rough logo, a layout sketch, a diagram of “how the pieces connect.”

**Not good for:** producing the actual app. Use the picture as a reference, then build the thing in chat or an editor.

## Brand examples

These names will go stale. The **categories** above should not. If a name looks wrong, [open an issue](https://github.com/1ststepai/ai-user-starter-kit/issues).

<!-- catalog:examples:start -->
_Examples as of September 2026._ Names change; the categories above do not.

| Category | Examples |
| --- | --- |
| Chat | ChatGPT, Claude.ai, Gemini |
| IDE agent | Cursor, other editors with a built-in agent |
| Terminal agent | Claude Code, Codex, similar command-line agents |
| Image | image modes in ChatGPT, Gemini, similar image tools |
<!-- catalog:examples:end -->

The table is generated from [`data/catalog.json`](../data/catalog.json). Refresh it with `python3 scripts/update-kit.py`.

## A simple chooser

| You want to… | Start with |
| --- | --- |
| Ask questions and draft text | Chat |
| Change files in a project and see the edits | IDE agent |
| Run tests and commands from a terminal | Terminal agent |
| Sketch a look or a diagram | Image |

If two rows both fit, pick the one you will actually open tomorrow.

## How to pick your one tool

1. Use what you already have access to. A free chat is enough to start.
2. If you write code in an editor, pick that editor’s agent.
3. If you live in the terminal and like it, pick a terminal agent.
4. Ignore launch-week hype. Ignore “everyone switched to X.”
5. Give the choice seven days before you re-evaluate.

You can try a second tool next week. First, get one small project across the finish line.

## Words you’ll see

- **Prompt** — what you type to the AI.
- **Agent** — an AI that can edit files or run commands, not only chat.
- **Diff** — the list of changes. Read it like a receipt.
- **Tokens** — pieces of text the model reads and writes. More text usually means more usage.
- **Hallucination** — a confident answer that is made up. See [Safety and trust](safety-and-trust.md).

## Next

Open the [first-week playbook](first-week-playbook.md) and start a project small enough to finish.

---

[Kit home](index.md) · [Playbook](first-week-playbook.md) · [Hygiene](usage-hygiene.md) · [Safety](safety-and-trust.md) · [What’s updated](CHANGELOG.md)
