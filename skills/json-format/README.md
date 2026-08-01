# json-format

> Use this skill to pretty-print or minify a JSON string (mode=pretty|minify, optional sort_keys). Validates first. Deterministic, offline.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/json-format
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
| `mode` | string | no | pretty (default) or minify |
| `sort_keys` | boolean | no | sort object keys |

## License

Proprietary — © SkillForge
