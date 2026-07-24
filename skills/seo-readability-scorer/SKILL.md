---
name: seo-readability-scorer
description: "Use this skill to score text for SEO readability: Flesch reading ease, avg sentence length, word count, passive-voice hints, and keyword density for a target keyword. Deterministic, offline, no dependencies. Great for grading blog drafts before publishing."
compatibility: ">=1.0"
---

# seo-readability-scorer

Use this skill to score text for SEO readability: Flesch reading ease, avg sentence length, word count, passive-voice hints, and keyword density for a target keyword. Deterministic, offline, no dependencies. Great for grading blog drafts before publishing.

- **Kind**: analyzer  |  **Niche**: publishing  |  **Cost tier**: free  |  **Version**: 0.1.0

## Empire Integration
```python
import sys
sys.path.insert(0, r'C:\D\Claude Code Projects\_SHARED')
import empire_bootstrap  # wires all shared paths
```

## Usage

**As a CLI:**
```bash
python run.py --text <string>
```

**From a Python agent (ATEN runtime):**
```python
from skill_library import executor
result = executor.execute("seo-readability-scorer", {text=...})
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | The text to score |
| `keyword` | string | no | Target keyword for density |

## Returns

`object` — `{"status": "ok"|"error", "result": ...}`
