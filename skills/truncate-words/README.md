# truncate-words

> Use this skill to truncate text to a max number of words with an ellipsis (default 50). Deterministic, offline. For excerpts and previews.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/truncate-words
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Input text |
| `words` | number | no | Max words (default 50) |

## License

Proprietary — © SkillForge
