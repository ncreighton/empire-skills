---
name: content-calendar-generator
description: "Generate AI-powered monthly content calendars from trending topics, seasonal events, and keyword gaps. Use when the user needs SEO content planning, editorial calendars, or multi-channel content strategies for blogs, social media, and email."
version: 1.0.0
homepage: https://github.com/ncreighton/empire-skills
metadata:
  {
    "openclaw": {
      "requires": {
        "env": ["OPENAI_API_KEY", "GOOGLE_TRENDS_API_KEY"],
        "bins": []
      },
      "os": ["macos", "linux", "win32"],
      "files": ["SKILL.md"],
      "emoji": "📅"
    }
  }
---

# Content Calendar Generator

## Overview

The **Content Calendar Generator** is an AI-powered skill that automates the creation of strategic, data-driven monthly content calendars. It synthesizes trending topics from Google Trends, identifies seasonal opportunities, performs keyword gap analysis, and generates a comprehensive editorial roadmap optimized for SEO performance.

This skill eliminates the manual research overhead of content planning by:
- **Analyzing real-time trends** via Google Trends API
- **Identifying keyword gaps** in your niche using semantic search
- **Mapping seasonal events** and industry milestones
- **Generating content briefs** with SEO recommendations
- **Exporting to multiple formats** (CSV, JSON, Markdown, Google Sheets)
- **Integrating with WordPress, Slack, and email workflows**

Perfect for content strategists, marketing teams, and agencies managing multiple content streams. Supports blogs, social media, email newsletters, and video content planning.

---

## Quick Start

Try these prompts immediately to see the skill in action:

### Example 1: Basic Monthly Calendar
```
Generate a content calendar for my SaaS product management blog for March 2025.
Focus on trending topics in project management and agile methodologies.
Include 12-15 content pieces with SEO keywords and publish dates.
```

### Example 2: Seasonal + Keyword Gap Analysis
```
Create a 30-day content calendar for an e-commerce fashion brand.
Include seasonal spring trends, holiday events, and keyword gaps.
Identify 20 high-intent keywords we're not currently ranking for.
Format as CSV with columns: Date, Title, Topic, Primary Keyword, Content Type, Estimated Traffic.
```

### Example 3: Multi-Channel Strategy
```
Build a content calendar for Q2 2025 covering blog posts, LinkedIn articles, 
and email newsletter content for a B2B SaaS company in HR tech.
Prioritize trending topics in employee engagement and remote work.
Include content pillars, CTAs, and cross-promotion opportunities.
Export as JSON with metadata for WordPress integration.
```

### Example 4: Competitive Gap Analysis
```
Generate a content calendar for a fitness niche blog.
Analyze my top 5 competitors' content strategies.
Identify content gaps and untapped keyword opportunities.
Create 25 unique content ideas with difficulty scores and traffic estimates.
```

---

## Capabilities

### 1. Trend Analysis & Topic Discovery
- Pulls real-time trending topics from **Google Trends API**
- Analyzes search volume velocity and seasonal patterns
- Identifies emerging topics in your industry vertical
- Filters for relevance to your niche and audience
- Ranks topics by traffic potential and competition level

**Usage Example:**
```
Analyze trending topics in "sustainable fashion" for the next 90 days.
Show search volume trends, related queries, and rising topics.
Recommend which trends are worth creating content around.
```

### 2. Keyword Gap Analysis
- Compares your current content against competitor keyword coverage
- Identifies high-intent keywords you're not targeting
- Calculates keyword difficulty and traffic potential
- Groups keywords into content clusters (topic modeling)
- Recommends content pieces to fill gaps

**Usage Example:**
```
Analyze keyword gaps for my fitness blog vs. top 10 competitors.
Focus on long-tail keywords with 500-2000 monthly searches.
Show which keywords have low competition but high relevance.
```

### 3. Seasonal & Event Mapping
- Automatically detects relevant holidays, industry events, and seasonal peaks
- Maps content opportunities to peak search periods
- Creates themed content clusters around major events
- Provides lead-time recommendations (when to publish before events)
- Includes historical performance data for recurring events

**Usage Example:**
```
Map seasonal content opportunities for a gardening blog for 2025.
Include spring planting season, summer maintenance, fall prep, and winter planning.
Show optimal publish dates to rank before peak search periods.
```

### 4. Content Brief Generation
- Generates SEO-optimized content briefs for each calendar item
- Includes target keywords, search intent, outline structure
- Recommends content format (blog, video, infographic, email)
- Suggests internal linking opportunities
- Provides estimated word count and reading time

**Usage Example:**
```
Generate detailed content briefs for 10 blog posts in my calendar.
Include target keywords, search intent analysis, H2/H3 structure,
internal linking suggestions, and estimated traffic potential.
```

### 5. Multi-Format Export & Integration
- **CSV/Excel**: Import directly into project management tools
- **JSON**: API-ready for custom integrations
- **Markdown**: Ready for GitHub wikis and documentation
- **Google Sheets**: Auto-populate with formulas and formatting
- **WordPress XML**: Direct import into WordPress editorial calendar
- **Slack**: Push calendar to team channels with notifications
- **Zapier/Make**: Trigger workflows for content creation and scheduling

**Usage Example:**
```
Export the calendar as a Google Sheet with formulas for:
- Days until publish date
- Content status tracking (draft, editing, published)
- Traffic performance vs. forecast
- Auto-update from WordPress API
```

### 6. Content Performance Forecasting
- Estimates traffic potential based on keyword difficulty and volume
- Predicts ranking timeline for new content
- Calculates ROI by content type and topic cluster
- Recommends content repurposing opportunities
- Provides competitive benchmarking

---

## Configuration

### Required Environment Variables

```bash
# OpenAI API key for content generation and analysis
export OPENAI_API_KEY="sk-..."

# Google Trends and Search Console API credentials
export GOOGLE_TRENDS_API_KEY="your-api-key"
export GOOGLE_SEARCH_CONSOLE_PROPERTY="https://your-domain.com"

# Optional: Content management system integrations
export WORDPRESS_API_URL="https://your-site.com/wp-json"
export WORDPRESS_API_TOKEN="your-jwt-token"

export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
export GOOGLE_SHEETS_API_KEY="your-sheets-api-key"
```

### Configuration Options

```json
{
  "calendar_length": "30",
  "content_types": ["blog", "social", "email", "video"],
  "target_audience": "B2B SaaS decision makers",
  "niche": "project management software",
  "competitors": ["asana.com", "monday.com", "jira.com"],
  "min_search_volume": 100,
  "max_keyword_difficulty": 50,
  "focus_regions": ["US", "UK", "CA"],
  "languages": ["en"],
  "publication_frequency": "3-4 posts per week",
  "include_seasonal_events": true,
  "include_competitor_analysis": true,
  "export_formats": ["csv", "json", "google_sheets"],
  "auto_publish_schedule": false
}
```

### Setup Instructions

1. **Obtain API Keys**
   - Google Cloud: Enable Trends API and Search Console API
   - OpenAI: Create API key at platform.openai.com
   - WordPress (optional): Generate JWT token in plugin settings

2. **Environment Configuration**
   ```bash
   # Save to .env file
   source .env
   ```

3. **Verify Integrations**
   ```bash
   # Test Google Trends connection
   openclaw test-connection --service google-trends
   
   # Test WordPress integration
   openclaw test-connection --service wordpress
   ```

4. **First Run**
   ```bash
   openclaw run content-calendar-generator \
     --niche "your-niche" \
     --calendar-length 30 \
     --export-format csv
   ```

---

## Example Outputs

### Output 1: CSV Calendar Format
```
Date,Title,Topic,Primary Keyword,Content Type,Estimated Traffic,Keyword Difficulty,Search Intent,Status
2025-03-01,10 Project Management Tips for Remote Teams,Remote Work,project management remote teams,Blog,450,35,Informational,Draft
2025-03-03,Agile Retrospectives: Complete Guide,Agile,agile retrospectives,Blog,320,28,Informational,Draft
2025-03-05,5 Mistakes Killing Your Sprint Planning,Sprint Planning,sprint planning mistakes,Blog,280,32,Problem-solving,Planning
2025-03-08,Kanban vs Scrum: Detailed Comparison,Methodology,kanban vs scrum,Blog,890,42,Comparison,Scheduled
2025-03-10,Team Collaboration Tools 2025 Review,Tools,best team collaboration tools,Roundup,620,38,Comparison,Draft
```

### Output 2: JSON with Metadata
```json
{
  "calendar_meta": {
    "month": "March 2025",
    "total_pieces": 15,
    "estimated_total_traffic": 8940,
    "average_difficulty": 35.2,
    "coverage": {
      "blog": 10,
      "social": 3,
      "email": 2
    }
  },
  "calendar_items": [
    {
      "id": "2025-03-001",
      "publish_date": "2025-03-01",
      "title": "10 Project Management Tips for Remote Teams",
      "primary_keyword": "project management remote teams",
      "related_keywords": [
        "remote team management",
        "distributed team productivity",
        "asynchronous collaboration"
      ],
      "content_type": "blog",
      "estimated_traffic": 450,
      "keyword_difficulty": 35,
      "search_intent": "informational",
      "outline": [
        "Introduction: Why remote PM is different",
        "Tip 1: Clear communication protocols",
        "Tip 2: Asynchronous-first mindset",
        "Tip 3: Regular sync touchpoints",
        "Conclusion: Tools aren't enough"
      ],
      "internal_links": [
        "asynchronous-collaboration-guide",
        "communication-tools-comparison"
      ],
      "cta": "Download our Remote Team Playbook",
      "estimated_word_count": 2200,
      "competitor_coverage": 0.7
    }
  ]
}
```

### Output 3: Google Sheets Integration
Automatically creates a shared Google Sheet with:
- Color-coded status tracking (Draft → Editing → Published)
- Formulas for days-until-publish countdown
- Traffic forecasts vs. actual performance
- Team assignment and ownership
- Links to published content and analytics

---

## Tips & Best Practices

### 1. Start with Your Audience, Not Keywords
```
❌ Wrong: "Generate calendar for all marketing keywords"
✅ Right: "Generate calendar for B2B SaaS CFOs interested in 
           financial automation and cost reduction"
```
The skill performs better when you define your target persona first.

### 2. Leverage Competitor Analysis
- Provide 3-5 top competitors for gap analysis
- The skill identifies content they're ranking for that you're not
- Prioritize "quick wins" (low difficulty, relevant keywords)
- Use for differentiation opportunities, not copying

### 3. Balance Trend-Chasing with Evergreen Content
The calendar automatically allocates:
- **60% Evergreen**: Timeless content that ranks long-term
- **30% Seasonal**: Holiday and event-driven content
- **10% Trending**: Hot topics with short shelf life

Adjust ratios based on your content strategy.

### 4. Optimal Publish Frequency
```
Blog posts: 2-3 per week (consistent ranking signals)
Social media: 4-5 per week (engagement, not ranking)
Email: 1-2 per week (subscriber retention)
```
The skill respects your configured frequency.

### 5. Content Repurposing Strategy
One blog post can become:
- 3-5 social media posts (LinkedIn, Twitter, Instagram)
- 1 email newsletter feature
- 1 video script
- 1 infographic
- 1 podcast episode outline

Use the JSON export to create repurposing workflows.

### 6. Timing Matters for Seasonal Content
- **3-4 weeks before**: Publish major seasonal content
- **2 weeks before**: Publish supporting content
- **1 week before**: Social amplification and email teasers
- **During event**: Real-time updates and live content

The skill recommends optimal publish dates automatically.

### 7. Monitor and Iterate
- Track actual traffic vs. forecasts
- Update keyword difficulty monthly (it changes)
- Identify underperforming topics early
- Reallocate resources to high-performers

Export performance data to refine next month's calendar.

---

## Safety & Guardrails

### What This Skill WILL Do
✅ Analyze public data (Google Trends, search volume, competitor websites)
✅ Generate content ideas and strategic recommendations
✅ Create editorial calendars and briefs
✅ Suggest SEO optimizations and keyword targets
✅ Export data to your tools (WordPress, Google Sheets, etc.)

### What This Skill WILL NOT Do
❌ **Plagiarize or copy competitor content** — It identifies gaps, not copy opportunities
❌ **Create actual written content** — It generates briefs and outlines only; you write the content
❌ **Guarantee rankings** — SEO results depend on content quality, backlinks, and user experience
❌ **Violate robots.txt or scrape protected content** — Uses only public APIs and ethical data sources
❌ **Bypass WordPress authentication** — Requires valid API tokens for integrations
❌ **Make financial predictions** — Traffic estimates are forecasts, not guarantees
❌ **Target private/protected keywords** — Respects robots.txt and terms of service

### Ethical Boundaries
- **Competitor analysis** is limited to public, indexed content only
- **Keyword recommendations** exclude adult, illegal, or harmful niches
- **Content suggestions** comply with platform guidelines (YouTube, TikTok, LinkedIn policies)
- **Data privacy**: No personal data collection; respects GDPR/CCPA compliance
- **Rate limiting**: Respects API quotas to avoid service disruption

### Limitations
- **Google Trends data** has a 3-day lag (not real-time)
- **Keyword difficulty** is estimated; actual difficulty varies by domain authority
- **Traffic forecasts** assume average CTR and ranking position; your results may differ
- **Competitor data** is limited to publicly indexed pages (no private content)
- **Seasonal events** are US-centric by default; customize for other regions

### Content Guardrails
The skill will refuse to generate calendars for:
- Adult/NSFW content
- Illegal products or services
- Misinformation or medical advice (without expert review)
- Hateful, discriminatory, or harassing content
- Spam or low-quality content farms

---

## Troubleshooting

### Q: "Google Trends API returns no data"
**A:** Google Trends has rate limits. Solutions:
- Increase API quota in Google Cloud Console
- Narrow your search scope (specific region, language)
- Try again in 1 hour (rate limit resets)
- Verify API key has Trends API enabled

### Q: "Keyword difficulty scores seem inaccurate"
**A:** Difficulty is estimated from:
- Search volume
- SERP feature count
- Average domain authority of top 10 results
- Your own domain authority

For more accuracy, integrate with Ahrefs, SEMrush, or Moz API.

### Q: "Calendar items don't match my niche"
**A:** Improve results by being specific:
```
❌ "Generate calendar for tech"
✅ "Generate calendar for B2B SaaS project management tools, 
     targeting CTOs and engineering leaders, focused on 
     enterprise features and remote team collaboration"
```

### Q: "WordPress integration failing"
**A:** Common causes:
1. JWT token expired → Regenerate in WordPress plugin
2. API URL incorrect → Verify `https://your-site.com/wp-json` is accessible
3. Insufficient permissions → Ensure token has Editor+ role
4. Firewall blocking → Check server logs for IP blocks

Test with:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  https