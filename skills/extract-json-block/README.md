# extract-json-block

> Use this skill to pull the first valid JSON object or array out of noisy or LLM-generated text: strips ```json code fences, does a balanced-brace scan, and repairs trailing commas. Returns the parsed data. Deterministic, offline. Essential for safely parsing LLM output before using it.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/extract-json-block
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text that contains JSON somewhere |

## License

Proprietary — © SkillForge
