# rewrite-tone

> Use this skill to rewrite text in a target tone (e.g. professional, friendly, punchy, formal) while preserving meaning. Uses an LLM.

`v0.1.0` `tool` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/rewrite-tone
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string> --tone <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Input text |
| `tone` | string | yes | Target tone |

## License

Proprietary — © SkillForge
