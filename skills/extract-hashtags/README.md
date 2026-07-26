# extract-hashtags

> Use this skill to extract hashtags from social text: pulls #tags, de-duplicates case-insensitively, drops numeric-only tags, and returns them both with and without the # prefix. Deterministic, offline. Useful for auditing or reusing the tag set of a post.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/extract-hashtags
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Social post text |

## License

Proprietary — © SkillForge
