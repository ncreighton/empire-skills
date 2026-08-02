# classify-sentiment

> Use this skill to classify the sentiment of a short text as positive, negative, or neutral, with a one-line reason. Uses an LLM. For review/comment triage.

`v0.1.0` `analyzer` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/classify-sentiment
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
