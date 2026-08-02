# email-subject-lines

> Use this skill to generate N catchy email subject lines from an email body or topic, optimized for open rate (curiosity, brevity, no spam words). Uses an LLM. Returns a list.

`v0.1.0` `tool` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/email-subject-lines
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
| `count` | number | no | How many subject lines (default 5) |

## License

Proprietary — © SkillForge
