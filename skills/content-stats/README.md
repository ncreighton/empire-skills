# content-stats

> Use this skill to get objective stats for a piece of text: word count, character count, sentence count, paragraph count, and estimated reading time in minutes (at 220 wpm). Deterministic, offline, no dependencies. Good for grading draft length before publishing.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/content-stats
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to analyze |
| `wpm` | number | no | Reading speed (default 220) |

## License

Proprietary — © SkillForge
