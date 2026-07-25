# html-to-text

> Use this skill to convert HTML into clean plain text: removes script/style, turns block tags and <br> into newlines, strips remaining tags, unescapes HTML entities, and collapses whitespace. Deterministic, offline. The right first step before readability, word-count, or slop analysis on scraped or WordPress HTML.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/html-to-text
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --html <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `html` | string | yes | HTML string to convert |

## License

Proprietary — © SkillForge
