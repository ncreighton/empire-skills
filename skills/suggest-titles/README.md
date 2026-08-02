# suggest-titles

> Use this skill to generate N catchy, SEO-aware title options for an article given its topic or first paragraph. Uses an LLM.

`v0.1.0` `tool` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/suggest-titles
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
| `count` | number | no | How many titles (default 5) |

## License

Proprietary — © SkillForge
