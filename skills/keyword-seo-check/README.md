# keyword-seo-check

> Use this skill to check whether a target keyword appears in the title and slug (and at the title start) and returns an SEO placement score. Deterministic, offline. For on-page SEO validation.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/keyword-seo-check
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --keyword <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keyword` | string | yes | Target keyword |
| `title` | string | no | Post title |
| `slug` | string | no | Post slug |

## License

Proprietary — © SkillForge
