# link-audit

> Use this skill to audit markdown links: counts internal vs external (by site_domain) and checks the 3-5 internal-links-per-post convention. Deterministic, offline. For SEO link hygiene.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/link-audit
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --markdown <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `markdown` | string | yes | Markdown/HTML content |
| `site_domain` | string | no | Your domain, e.g. wealthfromai.com |

## License

Proprietary — © SkillForge
