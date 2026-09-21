---
title: Usage hygiene
---

# Usage hygiene

AI tools cost something — money, a monthly quota, or both. That is normal. This page is about staying aware, not about being afraid of a progress bar.

You do not need to optimize spend in week one. You do need a few habits so a curious afternoon does not become a mess.

## Cost without the scare story

- **Tokens** are pieces of text the model reads and writes. Long chats and big files use more.
- Pasting an entire project “just in case” is the usual way people burn quota.
- A cheap or *fast* model is enough for renames, explanations, and small edits.
- A slower, more *careful* model is for messy bugs, design choices, and anything hard to undo.
- Hitting a limit is a pause, not a verdict on whether you are “good at this.”

If you are still learning the tool, stay on the default or faster model until you have a reason to switch.

## Fast vs careful, in plain English

| Reach for | When |
| --- | --- |
| **Fast / lighter** | Short questions, tidy a paragraph, rename something, explain a file |
| **Careful / heavier** | You do not understand the bug, the change spans many files, or a mistake would be expensive |

If you are not sure, start light. Escalate after a clear miss — and say so in the next prompt: “The quick pass failed. Slow down and check X.”

You do not need a special router to do this by hand. Pick the model in the UI the same way you pick a screwdriver.

## Do not paste secrets

Never drop these into a chat, a prompt, or a screenshot:

- API keys, tokens, and passwords
- `.env` files and connection strings
- Private customer lists, medical notes, or payroll
- SSH keys, recovery codes, and 2FA backups
- Other people’s data you would not post on a public webpage

If the AI asks for a key, give it a **fake** placeholder like `YOUR_API_KEY` and keep the real value on your machine.

If you already pasted a real key, treat it as leaked: revoke it in that product’s dashboard and make a new one. Then read [safety and trust](safety-and-trust.md).

## Do not let agents run wild

In week one, keep the blast radius small:

- Work in a practice folder, not your job’s production app
- Do not point an agent at a live server, a paid cloud account, or a customer database
- Turn off or skip “auto-run all commands” until you can read what it wants to run
- Say “ask before you run anything destructive” if the tool supports that
- Watch for commands that delete files, force-push git, or change permissions

An agent that can run commands is helpful. It is also a very fast intern with no fear.

## Verify before you commit or push

The AI can write a perfect-looking commit message for a change you do not understand. That is not a save. That is a time bomb.

Before `git commit`:

- [ ] I can say what changed in one sentence
- [ ] I opened the diff and recognized every file
- [ ] I ran or clicked the thing I changed
- [ ] I did not commit `.env`, keys, or a surprise `node_modules`

Before `git push`:

- [ ] I meant to share this copy, not a private experiment
- [ ] The remote is the repo I think it is
- [ ] I am not force-pushing because a chat told me to

No git yet? Duplicate the folder first. Pushing is optional. Understanding the files is not.

## Keep the chat on a diet

- Start a new thread when the task changes
- Point at one file instead of zipping the whole project
- Ask for a summary, then delete or archive the old thread
- Do not paste logs that include cookies, tokens, or home directory paths you do not need

Less leftover context usually means cheaper, clearer answers.

## Next

Read [safety and trust](safety-and-trust.md) for the “can I believe this?” half of the same habit.

---

[Kit home](index.md) · [Starter map](starter-map.md) · [Playbook](first-week-playbook.md) · [Safety](safety-and-trust.md)
