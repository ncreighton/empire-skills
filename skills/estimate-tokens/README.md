# estimate-tokens

> Use this skill to approximate the LLM token count of a text before an API call, for cost/budget guarding. Averages two estimators (~4 chars/token and ~0.75 tokens/word). Deterministic, offline, no tokenizer dependency. Not exact, but reliable for gating oversized prompts.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/estimate-tokens
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to estimate |

## License

Proprietary — © SkillForge
