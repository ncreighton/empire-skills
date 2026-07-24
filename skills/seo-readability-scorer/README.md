# seo-readability-scorer

> Use this skill to score text for SEO readability: Flesch reading ease, avg sentence length, word count, passive-voice hints, and keyword density for a target keyword. Deterministic, offline, no dependencies. Great for grading blog drafts before publishing.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/seo-readability-scorer
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | The text to score |
| `keyword` | string | no | Target keyword for density |

## License

Proprietary — © SkillForge
