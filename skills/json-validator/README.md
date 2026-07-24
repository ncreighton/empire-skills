# json-validator

> Use this skill to check whether a string is valid JSON and describe its shape: top-level type, key count (objects) or length (arrays), and the specific parse error with line/column if invalid. Deterministic, offline. Great for validating LLM output before using it.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/json-validator
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | The JSON string to validate |

## License

Proprietary — © SkillForge
