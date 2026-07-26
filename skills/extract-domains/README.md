# extract-domains

> Use this skill to extract and normalize the domains of all URLs in a text: strips www, ports, and paths, de-duplicates, and counts links per domain. Deterministic, offline. Ideal for auditing outbound/affiliate links in an article or checking link diversity.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/extract-domains
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text containing URLs |

## License

Proprietary — © SkillForge
