# base64

> Use this skill to base64-encode or -decode text (mode=encode|decode). Deterministic, offline. For tokens, data URIs, and encoding payloads.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/base64
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
| `mode` | string | no | encode (default) or decode |

## License

Proprietary — © SkillForge
