---
title: Safety and trust
---

# Safety and trust

_Last reviewed: September 2026._

Treat every model like a fast, overconfident junior teammate. Helpful. Not in charge.

If you remember one line from this page: **agent output is a draft until you understand it.**

## What the model can invent

Models predict likely next words. They do not look up a private truth about your computer unless a tool actually reads the file.

They can invent, with a straight face:

- functions, flags, and APIs that do not exist
- files that are not in your project
- “the official docs say…” when they do not
- a bugfix that only hides the error
- a security claim they have not checked

Confidence is not evidence. A tidy explanation is not a test.

When something sounds important, ask: “Which file did you read? Quote the line.” If it cannot, believe the file, not the chat.

## Never paste API keys

This is the same rule as [usage hygiene](usage-hygiene.md), because it is how people get hurt.

- Do not paste keys, cookies, or session tokens into a prompt
- Do not upload a screenshot of a dashboard that shows a secret
- Do not commit keys “just for now”
- Do not let an agent print secrets into a log you might share

If a key leaked, revoke it. Do not debate whether “it was only a test key.” Rotate it.

Public GitHub history is forever enough. Assume a pushed secret is public.

## Review the change like a PR

A *pull request* (PR) is a proposed change for another person to read. Review your own agent work the same way — even when you are the only reviewer.

Look for:

- files you did not ask to touch
- deleted tests or skipped checks
- new network calls, install commands, or permissions
- comments that say `temporary` or `trust me`
- copy that would embarrass you if a stranger cloned the repo

If you work with other people, do not merge an agent PR you did not read. “The AI wrote it” is not a review.

## Draft, then yours

A useful sequence:

1. Ask for a plan.
2. Accept only the next small edit.
3. Run or click it yourself.
4. Rewrite anything you could not explain to a friend.
5. Then commit.

You are not slower for doing this. You are keeping the project in *your* head. That is the point of the first week.

If you cannot maintain the result without the chat open, it is still a draft.

## A short trust checklist

- [ ] I know which files changed
- [ ] I tried the happy path myself
- [ ] I did not paste or commit a secret
- [ ] I would be willing to put my name on this change
- [ ] If this is wrong, I know how to undo it

If two boxes are unchecked, stop. Restart the chat or revert the files.

## You are still the operator

The tool can type. You decide what ships.

That is enough. You do not need a perfect setup, a paid stack, or a community to start. The [playbook](first-week-playbook.md) is the whole assignment.

---

[Kit home](index.md) · [Starter map](starter-map.md) · [Playbook](first-week-playbook.md) · [Hygiene](usage-hygiene.md) · [What’s updated](CHANGELOG.md)
