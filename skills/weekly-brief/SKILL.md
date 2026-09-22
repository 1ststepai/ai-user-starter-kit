---
name: weekly-brief
description: Build a short Monday brief from the user's own notes, calendar hints, or pasted updates. Do not invent news or metrics.
---

# Weekly brief

## When to use

The user wants a one-page brief for the week: what changed, what matters, what to do next.

## Steps

1. Ask what the brief is for (project, business, or personal learning) if it is not obvious.
2. Use only sources they paste or that are already in the project. If they want "latest AI news," ask them to paste links or accept that items will be marked *unverified*.
3. Write:
   - **Top 3** — ranked, one line each
   - **What changed** — bullets, source or "user note"
   - **Do this week** — at most five actions, smallest first
   - **Ignore** — noise they can skip
4. Keep it under 400 words.
5. If Auto Model Router is in play: this is `fast / local` unless they asked for a long unattended research crawl.

## Output shape

```markdown
# Weekly brief — <subject> — <date>

## Top 3
## What changed
## Do this week
## Ignore
```

## Do not

- Do not invent citations, traffic numbers, or product launches.
- Do not send the brief anywhere (email, Slack, social).
- Do not scrape vendor billing dashboards.
