---
name: file-organizer
description: Propose a folder structure and naming rule for a messy directory. Preview only. Never move, rename, or delete until the user confirms.
---

# File organizer

## When to use

A folder is messy. The user wants a plan, not a surprise rewrite of disk.

## Steps

1. Work only in the folder they name. If they did not name one, stop and ask.
2. List current top-level files and folders (names only).
3. Propose:
   - a folder tree
   - a naming rule (`YYYY-MM-DD_topic_type.ext` unless they have one)
   - a move table: current path → new path
4. Flag anything that looks like secrets, production, or customer data. Those stay put.
5. Stop. Wait for `confirm` (or a revised plan).
6. After confirm, do the moves they approved. Print a change log. Do not delete originals unless they explicitly ask.

## Output shape

```text
Proposed tree:
...
Naming rule:
...
Moves (N):
  old → new
Held back (secrets / unclear):
  ...
Confirm to apply, or say what to change.
```

## Do not

- Do not move, rename, or delete before confirm.
- Do not touch paths outside the named folder.
- Do not invent files that are not there.
