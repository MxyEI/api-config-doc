---
title: "Configure Skills"
description: "Extend Claude Code capabilities with Skills — install with a single command, ready to use immediately"
---


# Configure Skills


Skills are capability extension packs for Claude Code — they equip Claude with specialized domain knowledge, workflows, and toolchains. Install a Skill, and Claude gains a new ability.


## Install Skills


### Install via /plugin (Recommended)


Type `/plugin` in Claude Code to enter the plugin management interface. The built-in Marketplace sources from the [Anthropic official Skills repository](https://github.com/anthropics/skills), allowing you to browse, install, and manage directly:


```text filename="Claude Code Chat"
/plugin
```


![Claude Code /plugin Interface](/assets/claude-code/01-claude-code-plugin-interface.webp)


Search for the desired Skill in the **Discover** tab and install it with one click.


### Install via CLI


You can also install a specific Skill directly from the command line:


```text
claude install <skill-name>
```


## Skills Marketplace


In addition to the built-in Marketplace, there are excellent third-party Skills platforms:


### Skills.sh

An open Agent Skills ecosystem — search and install with a single command:


```text
npx skills find <query>
```


![Skills.sh](/assets/claude-code/02-skills-sh.webp)


### ClawHub

A community-driven Skills publishing platform with version management and semantic search:


![ClawHub](/assets/claude-code/03-clawhub.webp)


## Project-Level Skills: CLAUDE.md


Create a `CLAUDE.md` file in your project root. Claude Code automatically loads it on startup as project-level context and conventions:


```text filename="CLAUDE.md"
# Project Conventions

## Tech Stack
- Next.js 16 + TypeScript
- Tailwind CSS v4
- pnpm as package manager

## Coding Conventions
- Use PascalCase for component names
- Prefer Server Components
- Maintain at least 80% test coverage
```


> ℹ️ `CLAUDE.md` is the most common way to configure project-level Skills — no installation needed, just place it in the project root to take effect.


## Learn More


- [Anthropic Skills Official Repository](https://github.com/anthropics/skills) — Anthropic’s official Skills collection
- [Anthropic Skills Documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Skills.sh — Open Skills Ecosystem](https://skills.sh/)
- [ClawHub — Skills Publishing Platform](https://clawhub.ai/skills)
