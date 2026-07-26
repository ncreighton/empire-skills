# normalize-phone

> Use this skill to normalize a phone number to E.164 format (+<country><number>): strips formatting, applies a default country code for bare 10-digit US numbers, preserves an explicit +prefix, and flags whether the result is a plausible length. Deterministic, offline. For cleaning contact/lead data.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/normalize-phone
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --phone <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `phone` | string | yes | Phone number in any format |
| `default_country_code` | string | no | Country code for bare local numbers (default '1') |

## License

Proprietary — © SkillForge
