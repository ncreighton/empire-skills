# smart-truncate

> Use this skill to truncate text to a max length at a word boundary with an ellipsis, without cutting words in half. Ideal for meta descriptions (155 chars), social previews, and card summaries. Deterministic, offline.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/smart-truncate
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to truncate |
| `max_length` | number | no | Max length incl ellipsis (default 155) |

## License

Proprietary — © SkillForge
