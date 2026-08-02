# uuid-check

> Use this skill to validate whether a string is a well-formed UUID (v1-v5) and report its version. Deterministic, offline. For ID validation.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/uuid-check
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --value <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | string | yes | String to check |

## License

Proprietary — © SkillForge
