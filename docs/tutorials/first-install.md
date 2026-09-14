# Your first install

By the end you will have the curated skills committed in a project, and you will have
watched an agent pick one of them for a task you describe in plain words.

You need git, Python 3.9 or later, and a project with a git repository in it.

## 1. Clone this repository

```bash
git clone https://github.com/yuusakuri/dev-skills
```

## 2. See what the default set contains

```bash
python3 dev-skills/scripts/install-skills.py --project . --list
```

The first line tells you the size of the set:

```
19 skills (core set) + development-lifecycle router
```

Below it, one line per skill, grouped by lifecycle phase. Every phase appears at least
once. Nothing has been written yet — `--list` only reports.

## 3. Install into your project

```bash
python3 dev-skills/scripts/install-skills.py --project /path/to/your-project
```

It writes `.claude/skills/` for Claude Code and `.agents/skills/` for the agents that
read the shared convention, plus `ATTRIBUTION.md` and a `licenses/` directory, because
the skills belong to their upstream authors.

## 4. Commit them

```bash
cd /path/to/your-project
git add .claude/skills .agents/skills
git commit -m "Add agent skills"
```

Anyone who clones the project now has the skills, with no per-developer setup step.

## 5. Watch the router choose

Open the project in Claude Code and ask, in plain words:

> Which skill covers deciding whether to ship a release?

You should see it answer `ship-gate`. You did not name a skill; the router matched your
description to a phase and named the skill that owns it.

If it cannot answer, the skills are not loaded. Restart the session and check that
`.claude/skills/` is really in the project you opened.

## What you have now

Twenty skills in the repository, and an agent that finds the right one from a
description. Next: [adopt it in a project](../how-to/adopt-in-a-project.md).
