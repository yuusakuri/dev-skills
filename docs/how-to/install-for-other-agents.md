# Install for agents other than Claude Code

Agent Skills are portable. Only the directory each agent reads differs, so installing
for another agent means writing the same files to another path.

## Write the directories your agents read

The default covers Claude Code and every agent that reads the shared `.agents/`
convention:

```bash
python3 dev-skills/scripts/install-skills.py --project .
```

For an agent with its own directory, name it:

```bash
python3 dev-skills/scripts/install-skills.py --project . --agents claude,gemini,cursor
python3 dev-skills/scripts/install-skills.py --project . --agents all
```

Names and directories: [reference/agent-directories.md](../reference/agent-directories.md).
Writing them all is cheap, because git stores one object per distinct file.

Do not install only `.agents/skills/`. Claude Code does not read it, and the failure is
silent: no error, just an agent that never mentions a skill.

## Let the agent install them itself

Gemini CLI can fetch skills directly with `gemini skills install <repo> --path skills`,
and the [skills CLI](https://github.com/vercel-labs/skills) covers 70+ agents one skill
at a time.

Take skills from the repository that authors them, at the ref pinned in
[`catalog.json`](../../catalog.json). Never from a mirror: mirrors drift, and copies in
circulation are already several revisions behind.
