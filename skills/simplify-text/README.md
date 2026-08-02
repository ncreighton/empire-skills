# simplify-text

> Use this skill to rewrite complex text in plain, simple language at a roughly 8th-grade reading level while preserving meaning. Uses an LLM.

`v0.1.0` `tool` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/simplify-text
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

## License

Proprietary — © SkillForge
