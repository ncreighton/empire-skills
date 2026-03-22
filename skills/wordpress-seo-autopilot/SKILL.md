---
name: wordpress-seo-autopilot
description: "Automate WordPress SEO optimization with meta tags, schema markup, internal linking, and RankMath integration. Use when the user needs on-page SEO, technical SEO audits, or bulk content optimization for WordPress sites."
version: 1.0.0
homepage: https://github.com/ncreighton/empire-skills
metadata:
  {
    "openclaw": {
      "requires": {
        "env": ["WORDPRESS_API_KEY", "WORDPRESS_SITE_URL", "RANKMATH_API_KEY", "GOOGLE_SEARCH_CONSOLE_KEY"],
        "bins": []
      },
      "os": ["macos", "linux", "win32"],
      "files": ["SKILL.md"],
      "emoji": "🚀"
    }
  }
---

## Overview

**WordPress SEO Autopilot** is a comprehensive SEO automation engine that transforms your WordPress site's search visibility through intelligent, data-driven optimization. This skill automates the tedious, repetitive tasks that consume hours of manual effort while maintaining best practices and brand consistency.

### Why This Matters

WordPress powers 43% of all websites, yet most site owners struggle with:
- **Manual meta tag creation** for hundreds of pages
- **Missing schema markup** that prevents rich snippets
- **Broken internal linking strategies** that waste link equity
- **Inconsistent SEO practices** across content
- **Slow RankMath configuration** for large sites

This skill eliminates these bottlenecks by integrating directly with WordPress REST API, RankMath's automation engine, and Google Search Console for real-time optimization based on actual search performance data.

### Key Integrations

- **WordPress REST API** — Direct post/page optimization
- **RankMath SEO** — Native integration for advanced features
- **Google Search Console** — Real-time search analytics
- **Slack** — Optimization reports and alerts
- **Google Sheets** — Bulk optimization workflows
- **Yoast SEO** (fallback) — Alternative plugin support

---

## Quick Start

Try these prompts immediately in your ClawHub interface:

### Example 1: Optimize All Posts for Target Keywords
```
Optimize all WordPress posts published in the last 30 days for SEO.
Target keywords: "sustainable packaging", "eco-friendly shipping", "green logistics".
Set meta descriptions to 155-160 characters.
Add schema markup for Product and Organization.
Update internal links to relevant posts.
Generate a Slack report with optimization score for each post.
```

### Example 2: Bulk Meta Tag Generation
```
Generate meta tags for my top 50 underperforming pages from Google Search Console.
Current average CTR: 2.1%, target: 4.5%.
Focus on title tags (55-60 chars) and meta descriptions (155-160 chars).
Include semantic keywords from RankMath analysis.
Preview changes before applying to WordPress.
```

### Example 3: Schema Markup Audit & Fix
```
Scan my WordPress site for missing schema markup.
Identify pages missing: Product schema, Article schema, Organization schema.
Auto-generate and apply appropriate schema based on post type.
Validate all schema with Google's Rich Results Test.
Report broken or incomplete markup to Slack.
```

### Example 4: Internal Linking Strategy
```
Analyze internal linking on my WordPress site.
Identify orphaned posts (fewer than 3 internal links).
Find high-authority posts with link equity to redistribute.
Suggest and implement contextual internal links for target keywords.
Create a link flow visualization showing improved site architecture.
```

---

## Capabilities

### 1. Intelligent Meta Tag Optimization

**What it does:**
- Generates SEO-optimized title tags (50-60 characters)
- Creates compelling meta descriptions (155-160 characters)
- Implements dynamic meta tags based on post content and keywords
- A/B tests multiple meta tag variations using Google Search Console data

**Usage example:**
```
Optimize meta tags for posts ranking in positions 4-10 on Google.
These are my CTR targets by search intent:
- Informational: 3.5%
- Commercial: 5.2%
- Transactional: 6.8%
Use power words: "Complete Guide", "Proven", "Step-by-Step", "Expert".
```

**Output:** Updated WordPress posts with optimized tags + preview of CTR improvements

### 2. Automated Schema Markup

**What it does:**
- Detects post type (article, product, service, event, etc.)
- Generates JSON-LD schema automatically
- Adds rich snippet eligibility (ratings, prices, dates)
- Validates schema against Google's requirements
- Implements breadcrumb schema for navigation

**Usage example:**
```
Add schema markup to all e-commerce product posts.
Include: Product schema with price, availability, rating.
Add AggregateOffer schema for product bundles.
Include FAQ schema for common questions in post content.
Validate with Google Rich Results Test API.
```

**Output:** Schema-enhanced posts + validation report + rich snippet preview

### 3. Strategic Internal Linking

**What it does:**
- Identifies link opportunities based on keyword matching
- Prevents orphaned content (posts with <3 internal links)
- Distributes link equity from high-authority pages
- Creates contextual, semantic links (not keyword-stuffed)
- Maintains link diversity across site sections

**Usage example:**
```
Build internal links for my pillar content strategy.
Pillar page: "Ultimate Guide to Content Marketing"
Cluster topics: SEO, copywriting, distribution, analytics.
Link each cluster post back to pillar with "content marketing" anchor.
Ensure 5-7 outbound links per cluster post.
Visualize link flow in a graph.
```

**Output:** Updated post content with new internal links + link flow diagram

### 4. RankMath Native Integration

**What it does:**
- Pushes optimizations directly to RankMath settings
- Leverages RankMath's content AI for suggestions
- Configures focus keywords and related keywords
- Automates RankMath's SEO score improvements
- Syncs with RankMath's Google Search Console data

**Usage example:**
```
Use RankMath to optimize all posts for E-E-A-T signals.
Set focus keywords from my content calendar.
Add author expertise schema with author bio.
Implement topical authority linking (cluster model).
Target RankMath SEO score of 85+ for all posts.
```

**Output:** Posts with RankMath optimization + E-E-A-T improvements

### 5. Google Search Console Integration

**What it does:**
- Analyzes actual search performance data
- Identifies high-impression, low-CTR pages
- Finds keyword opportunities (queries with low rankings)
- Prioritizes optimization based on search impact
- Tracks optimization results over time

**Usage example:**
```
Fix my top 20 underperforming queries in Google Search Console.
Show me: queries with 100+ impressions but <2% CTR.
Optimize title/meta for improved CTR.
Add schema to increase rich snippet eligibility.
Track improvements weekly and report to Slack.
```

**Output:** Priority optimization list + CTR improvement tracking

### 6. Bulk Optimization Workflows

**What it does:**
- Processes 10-1,000+ pages in a single workflow
- Applies consistent optimization rules across content
- Maintains brand voice and style guidelines
- Prevents over-optimization and keyword stuffing
- Creates before/after comparison reports

**Usage example:**
```
Bulk optimize 500 blog posts for my WordPress site.
Apply these rules:
- Title: [Primary Keyword] - [Modifier] | Brand Name (60 chars max)
- Meta: Action-oriented, include number or power word (155 chars)
- Schema: Article schema with author, date, image
- Links: 3-5 contextual internal links per post
- Preview all changes before applying.
```

**Output:** Bulk optimization report + preview dashboard + rollback option

---

## Configuration

### Required Environment Variables

Set these in your ClawHub environment before using this skill:

```bash
# WordPress REST API credentials
WORDPRESS_API_KEY=your_wordpress_rest_api_key
WORDPRESS_SITE_URL=https://yoursite.com

# RankMath API (get from RankMath dashboard > Settings > API)
RANKMATH_API_KEY=your_rankmath_api_key

# Google APIs
GOOGLE_SEARCH_CONSOLE_KEY=your_gsc_api_key
GOOGLE_SHEETS_API_KEY=your_sheets_api_key (optional, for bulk workflows)

# Slack Integration (optional, for reports)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL

# Optional: Content Guidelines
SEO_BRAND_VOICE=professional|conversational|technical
SEO_TARGET_KEYWORD_DENSITY=1-2%
SEO_MIN_WORD_COUNT=800
```

### Setup Instructions

1. **Generate WordPress REST API credentials:**
   - WordPress Admin → Settings → REST API
   - Create an application token with `posts:read`, `posts:edit`, `posts:create` permissions

2. **Enable RankMath API:**
   - RankMath → Settings → General → API
   - Copy API key and save to environment

3. **Connect Google Search Console:**
   - Go to Google Cloud Console
   - Enable Search Console API
   - Download service account JSON
   - Save key to `GOOGLE_SEARCH_CONSOLE_KEY`

4. **Optional: Set up Slack notifications:**
   - Create Slack webhook at api.slack.com/messaging/webhooks
   - Add URL to `SLACK_WEBHOOK_URL`

---

## Example Outputs

### Meta Tag Optimization Report

```
OPTIMIZATION SUMMARY
====================
Posts Processed: 47
Average Title Length: 58 characters ✓
Average Meta Description: 157 characters ✓
Estimated CTR Improvement: +2.3%

TOP OPPORTUNITIES (High Impression, Low CTR)
Post: "10 SEO Tips for WordPress"
Current: Impressions 1,240 | CTR 1.8% | Position 5.2
Suggested Title: "10 WordPress SEO Tips That Actually Work [2024 Guide]"
Suggested Meta: "Proven WordPress SEO strategies to boost rankings. Step-by-step guide with RankMath integration and schema markup examples."
Estimated New CTR: 3.5% (+1.7%)
```

### Schema Markup Validation Report

```
SCHEMA MARKUP AUDIT
===================
Total Pages Scanned: 127
Pages with Schema: 94 (74%)
Missing Schema: 33 (26%)

MISSING SCHEMA BREAKDOWN:
- Article Schema: 18 pages
- Organization Schema: 8 pages
- BreadcrumbList Schema: 7 pages

INVALID SCHEMA:
- Product Schema (price missing): 3 pages
- Author Schema (name missing): 2 pages

ACTION: Auto-fix all missing/invalid schema? [Y/n]
```

### Internal Linking Analysis

```
INTERNAL LINKING STRATEGY
==========================
Total Posts: 247
Orphaned Posts (0-2 links): 34
Well-Linked Posts (5+ links): 156

LINK EQUITY DISTRIBUTION:
Highest Authority (RankMath Score 92): "Complete WordPress Guide"
  → Can distribute 12 new links to cluster posts

RECOMMENDED LINKS TO ADD: 87
Estimated Link Equity Redistribution: +15% site-wide authority

LINK FLOW VISUALIZATION:
[Pillar Page] → [Cluster 1] → [Cluster 2] → [Cluster 3]
   (92)           (78)          (75)          (72)
```

### Slack Notification Example

```
🚀 WordPress SEO Autopilot - Weekly Optimization Report

📊 Performance This Week:
✓ 42 posts optimized
✓ 8 new schema implementations
✓ 127 internal links added
✓ Average CTR improvement: +1.8%

🎯 Top Performer:
"Advanced WordPress Security" - CTR ↑ 3.2% (Position 3→2)

⚠️ Needs Attention:
"WordPress Hosting Guide" - Still at position 8 (target: 5)
Suggested: Update meta tags + add FAQ schema

📈 Next Steps:
Fix 5 underperforming queries | Add schema to 12 new pages
```

---

## Tips & Best Practices

### 1. Start Small, Scale Gradually
- Begin with 20-50 posts to validate the optimization strategy
- Monitor Google Search Console for 2-4 weeks before scaling
- Use preview mode to review changes before applying
- Only auto-apply after confirming improvements

### 2. Align with Your Content Strategy
- Define your pillar content and topic clusters first
- Use internal linking to reinforce topical authority
- Ensure keywords match your business goals
- Avoid optimizing for vanity metrics (keyword difficulty)

### 3. Maintain Brand Voice
- Set `SEO_BRAND_VOICE` environment variable to match your style
- Review auto-generated meta tags for brand consistency
- Don't sacrifice clarity for keyword inclusion
- Test meta tags with real users before full rollout

### 4. Leverage Google Search Console Data
- Prioritize optimization based on actual search performance
- Focus on high-impression, low-CTR pages first (quick wins)
- Target keywords with 3-10 ranking positions (most improvable)
- Track CTR improvements weekly, not daily (Google's data lags)

### 5. Schema Markup Strategy
- Implement Article schema for blog posts (improves SERP appearance)
- Use Product schema for e-commerce (enables rich snippets)
- Add Organization schema to homepage (builds brand trust)
- Validate all schema with Google's Rich Results Test tool

### 6. Internal Linking Best Practices
- Use descriptive anchor text (not "click here" or exact keywords)
- Link contextually within post content (not just footer)
- Maintain 3-5 internal links per post (avoid over-linking)
- Create a hub-and-spoke model: pillar pages → cluster content

### 7. Monitor and Adjust
- Check Google Search Console weekly for ranking changes
- Track CTR improvements and adjust meta tags if needed
- Monitor for keyword cannibalization (multiple posts targeting same keyword)
- Review RankMath SEO scores monthly and improve lowest-scoring posts

---

## Safety & Guardrails

### What This Skill Will NOT Do

❌ **Keyword stuffing** — Meta tags and content remain natural and readable
❌ **Cloaking or hidden text** — All optimizations are transparent to users
❌ **Duplicate content** — Each page retains unique, valuable content
❌ **Manipulative schema** — Schema accurately represents actual content
❌ **Link schemes** — Internal links are contextual and valuable to users
❌ **Spammy link anchors** — Anchor text is descriptive and natural
❌ **Auto-publishing without review** — All changes require preview/approval
❌ **Over-optimization** — Maintains readability and user experience

### Limitations & Boundaries

**Rate Limiting:**
- WordPress API: 10 requests/second (skill respects this)
- Google Search Console: 100 queries/day (skill batches requests)
- RankMath API: 5 requests/second

**Content Constraints:**
- Meta descriptions: 155-160 characters (Google's display limit)
- Title tags: 50-60 characters (optimal for CTR)
- Minimum post length: 300 words (configurable)
- Maximum posts per batch: 1,000 (to prevent server overload)

**Geographic Considerations:**
- This skill optimizes for Google (US/English-speaking markets)
- For international sites, configure language-specific settings
- Schema markup follows schema.org standards (Google-compliant)

**Compliance Notes:**
- Does not create false or misleading content
- Does not violate WordPress plugin terms of service
- Does not bypass RankMath's content guidelines
- Respects robots.txt and noindex directives
- Complies with Google's Helpful Content Update guidelines

---

## Troubleshooting

### Common Issues & Solutions

**Issue: "WordPress API Key Invalid"**
```
Error: 401 Unauthorized - Check your WordPress REST API credentials
Solution:
1. Verify API key in WordPress Admin → Settings → REST API
2. Ensure API key has 'posts:read' and 'posts:edit' permissions
3. Check that WORDPRESS_SITE_URL includes https:// and no trailing slash
4. Test connection: curl -H "Authorization: Bearer YOUR_KEY" https://yoursite.com/wp-json/wp/v2/posts
```

**Issue: "RankMath API Connection Failed"**
```
Error: Cannot connect to RankMath API
Solution:
1. Verify RANKMATH_API_KEY is correct (RankMath → Settings → General → API)
2. Ensure RankMath Pro is activated