# summarize-bullets

> Use this skill to summarize a block of text into N concise bullet points capturing the key ideas. Uses an LLM. Good for TL;DRs and article recaps.

`v0.1.0` `tool` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/summarize-bullets
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
| `count` | number | no | Number of bullets (default 3) |

## License

Proprietary — © SkillForge
