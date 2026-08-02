# answer-faq

> Use this skill to generate a concise FAQ answer for a given question, optionally grounded in provided context text. Uses an LLM.

`v0.1.0` `tool` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/answer-faq
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --question <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `question` | string | yes | The question |
| `context` | string | no | Optional grounding context |

## License

Proprietary — © SkillForge
