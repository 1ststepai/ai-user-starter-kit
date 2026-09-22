---
name: skill-maker
description: Turn a repeat prompt or workflow into a short SKILL.md. Do not invent tools. Wait before writing files outside a skills folder.
---

# Skill maker

## When to use

The user has a prompt they reuse, or a 3–10 step job they want the agent to do the same way next time.

## Do this

1. Ask for the **outcome** in one sentence, the **inputs**, and what must never happen.
2. Draft a `SKILL.md` with YAML `name` + `description`, then: When to use, Steps, Output shape, Do not.
3. Keep it under ~80 lines. No vendor model names.
4. Show the draft. Wait for confirm before writing a file.
5. If they confirm, write only to a path they name (usually `.cursor/skills/<name>/SKILL.md`).

## Output shape

```markdown
---
name: kebab-case
description: One line that says when to load this skill.
---

# Title

## When to use
## Steps
## Output shape
## Do not
```

## Do not

- Do not add MCP servers, APIs, or paid tools the user did not ask for.
- Do not mark the skill as official 1stStep product policy unless they say so.
- Do not auto-continue spendy or irreversible work; point them at Auto Model Router if they have it.
