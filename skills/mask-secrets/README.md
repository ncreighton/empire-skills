# mask-secrets

> Use this skill to redact secrets from text before logging or sharing: masks OpenAI keys (sk-), GitHub PATs, AWS access keys, Slack tokens, Bearer tokens, and email addresses. Deterministic, offline. Returns the masked text and a redaction count.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/mask-secrets
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text possibly containing secrets |

## License

Proprietary — © SkillForge
