# word-wrap

> Use this skill to wrap text to a given column width (default 80), preserving words. Deterministic, offline. For plain-text formatting and emails.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/word-wrap
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to wrap |
| `width` | number | no | Column width (default 80) |

## License

Proprietary — © SkillForge
