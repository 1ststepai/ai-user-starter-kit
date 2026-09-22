---
name: geo-block
description: Rewrite one page section into a 40–60 word quotable answer block plus entities. Do not invent citations or schema the page cannot support.
---

# GEO block

Generative Engine Optimization for one page. Goal: a self-contained answer an AI overview could quote without lying.

## When to use

The user has a URL, draft, or heading and wants that section to be citable — not a full SEO audit.

## Steps

1. Read the section they give. If there is no source text, ask for it. Do not write from a keyword alone.
2. Write one **answer block** of 40–60 words: complete sentence(s), no "in this article," no hype.
3. List **entities** that already appear (product, org, place). Do not add famous names that are not in the text.
4. Suggest one H2 and one FAQ question that the block actually answers.
5. Optional JSON-LD *only* for FAQ/HowTo that matches the text. No fake Review or AggregateRating.
6. Stop. They paste. You do not publish.

## Output shape

```markdown
## Answer block (40–60 words)
...

## Entities found in source
- ...

## Suggested H2
## Suggested FAQ
## JSON-LD (optional, only if supported by the text)
```

## Do not

- Do not invent statistics or outbound citations.
- Do not claim the page will rank in Google or be cited by ChatGPT.
- Do not rewrite the whole site in one pass.
