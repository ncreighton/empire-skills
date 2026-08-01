# case-convert

> Use this skill to convert an identifier between snake_case, camelCase, PascalCase, and kebab-case (to=snake|camel|pascal|kebab). Deterministic, offline. For code/config transforms.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/case-convert
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
| `to` | string | no | snake\|camel\|pascal\|kebab (default snake) |

## License

Proprietary — © SkillForge
