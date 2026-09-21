---
title: First-week playbook
---

# First-week playbook

_Last reviewed: September 2026._

Goal for the week: finish **one small project** you understand well enough to change without the AI.

Not a startup. Not a rewrite of your job. A practice project you can throw away.

## The daily loop

Use this every day, even when you skip the numbered plan:

1. Ask for **one** small change.
2. Read the plan or the *diff* (the list of edits) before you accept it.
3. Try it.
4. Check it yourself — click, run, or read the result.
5. Keep it or undo it.
6. If the chat is lost, **start a new one**.

That loop matters more than the perfect prompt.

## Prompts that work early

Ask for a plan first. Keep the task small. Say what “done” looks like.

> I want a single-file personal homepage: my name, three links, and a two-sentence bio. HTML and CSS only. List the steps, then wait.

> Explain `main.py` like I am new. Do not change any files.

> Propose a small change. Show the diff. Do not apply it until I say yes.

> This failed. Here is the exact error. Suggest one next check, not a rewrite.

You can copy those and swap in your filenames.

## When to read the diff

Read it:

- before you accept edits that touch more than a few lines
- anytime you do not recognize a filename
- before every commit
- when the AI says “I also cleaned a few things up”

If you cannot explain the change in one sentence, do not keep it yet. Ask: “What did you change, file by file, in plain English?”

## When to stop and restart the chat

Start a new chat when:

- it keeps “fixing” the same bug
- it edits files you did not mention
- the thread is long and it forgot your first rule
- you feel lost and are just clicking Accept

A new chat is not failure. Long confused chats waste more time than a clean restart.

Copy a short recap into the new thread: what the project is, what already works, and the one thing you want next.

## Seven days

Skip a day if life happens. Do not “catch up” by doing three projects on Sunday.

### Day 1 — Arrive

Install or open **one** tool from the [starter map](starter-map.md).

Create a folder named something like `practice-week`. Tell the AI that this folder is the only place it may change.

Ask it to create the smallest possible “hello” — a page that says your name, or a script that prints `hello`.

**Done when:** you can find the file and open or run it without the AI.

### Day 2 — Pick the project

Choose one:

- a personal homepage
- a todo list you can add and check off
- a script that renames files in a sample folder
- a flashcard page for something you are actually learning

Write three bullets: who it is for (you), what it does, and what it will *not* do this week.

**Done when:** you have those three bullets saved in a `README` or a note.

### Day 3 — Make it real, still small

Build the first useful version. One happy path. No accounts, no database, no “while we’re here.”

If the AI offers a framework you have never heard of, say: “Stay with the simplest files. Explain any new file before you add it.”

**Done when:** you can use the main feature once.

### Day 4 — Prompt on purpose

Do three asks:

1. A tiny visual or wording improvement.
2. An explanation of one file you do not understand.
3. A change you then **reject**, and a better version you accept.

Practice saying no. The skill is steering, not collecting code.

**Done when:** you rejected at least one suggestion on purpose.

### Day 5 — Break it and recover

Change one thing until it fails — a typo, a missing file, a wrong click.

Paste the exact error. Ask for **one** next check. Do not accept a full rewrite.

**Done when:** it works again and you can say what was wrong in one sentence.

### Day 6 — Save your work

If you use git, make a small commit you wrote the message for.

If you do not use git yet, copy the folder to a dated backup.

Read [usage hygiene](usage-hygiene.md) before you push anywhere public.

**Done when:** you have a snapshot you could return to.

### Day 7 — Review

Answer these, in writing:

- What did I build?
- Which change did I understand least?
- When did I restart a chat?
- What will I try next week — still one tool, still one project?

**Done when:** you could demo the project to a friend in five minutes.

## What “better prompts” actually means

It is not magic words. It is usually:

- **Scope:** one outcome, not five
- **Context:** the file, the error, the rule (“don’t add a new folder”)
- **Stop point:** “plan first” or “show the diff and wait”
- **Audience:** “I am new; define jargon once”

If a prompt is longer than the task, cut the prompt.

## Next

Read [usage hygiene](usage-hygiene.md) before you point an agent at anything you care about.

---

[Kit home](index.md) · [Starter map](starter-map.md) · [Hygiene](usage-hygiene.md) · [Safety](safety-and-trust.md) · [What’s updated](CHANGELOG.md)
