---
name: etsy-listing-optimizer
description: "Optimize Etsy titles, tags, and descriptions using keyword research and competitor analysis. Use when the user needs to increase search visibility, boost conversion rates, or improve SEO rankings for Etsy shop listings."
version: 1.0.0
homepage: https://github.com/ncreighton/empire-skills
metadata:
  {
    "openclaw": {
      "requires": {
        "env": ["ETSY_API_KEY", "GOOGLE_TRENDS_API_KEY"],
        "bins": []
      },
      "os": ["macos", "linux", "win32"],
      "files": ["SKILL.md"],
      "emoji": "🛍️"
    }
  }
---

# Etsy Listing Optimizer

## Overview

The Etsy Listing Optimizer is a comprehensive automation tool that transforms underperforming Etsy listings into high-converting, search-optimized product pages. This skill analyzes your current listings against competitor benchmarks, identifies high-intent keywords, and generates data-driven recommendations for titles, tags, and descriptions that rank higher in Etsy search and Google Shopping.

**Why this matters:**
- Etsy's search algorithm prioritizes listings with optimized titles and tags (40% of shop traffic comes from internal search)
- Competitors with better SEO can capture 3-5x more impressions for the same keywords
- A single optimized listing can increase monthly revenue by 20-40% through improved visibility

**Integrations:**
- **Etsy API** — Direct listing analysis and performance metrics
- **Google Trends** — Real-time keyword demand tracking
- **SimilarWeb** — Competitor shop analysis
- **Slack** — Batch optimization reports and alerts
- **Google Sheets** — Export optimization roadmaps for team collaboration

---

## Quick Start

Try these example prompts immediately:

### Example 1: Single Listing Optimization
```
Optimize my Etsy listing for a handmade ceramic mug.
Current title: "Blue Ceramic Mug"
Current tags: ceramic, mug, blue, handmade, gift
Current description: "A beautiful blue ceramic mug made by hand. Great for coffee or tea."
Target audience: Coffee enthusiasts aged 25-45
Budget: Mid-range ($25-35)
```

### Example 2: Batch Competitor Analysis
```
Analyze my 5 best-selling products against top 10 competitors in the "personalized wooden gifts" category.
My shop: [shop-name]
Competitor shops: [list 5-10 competitor shop names]
Focus areas: Title length, tag strategy, keyword density
Generate: A spreadsheet with side-by-side comparison and optimization gaps
```

### Example 3: Seasonal Keyword Research
```
Update my winter holiday listings for maximum visibility in Q4.
Current product: Handmade knit scarves
Seasonal trend data: Include search volume for "holiday gift", "winter scarf", "personalized gift"
Geographic focus: United States
Output: Revised titles, 13 optimized tags, and seasonal description angles
```

---

## Capabilities

### 1. Keyword Research & Analysis
- **Trend Detection**: Identifies rising search terms using Google Trends API with 90-day historical data
- **Search Volume Estimation**: Analyzes Etsy search bar autocomplete patterns to estimate monthly search volume
- **Competitor Keyword Mapping**: Scrapes top 20 competitor listings to identify keyword gaps and opportunities
- **Long-tail Keyword Discovery**: Generates 50+ long-tail variations for niche products
- **Seasonal Keyword Tracking**: Detects seasonal demand shifts and timing recommendations

**Usage Example:**
```
Analyze keyword opportunities for "vintage leather journals"
Show: search volume, competition level, seasonal trends, related keywords
Include: 5-year trend data and predicted Q1 2025 demand
```

### 2. Title Optimization
- **Character-count optimization**: Crafts titles within Etsy's 140-character limit while maximizing keyword density
- **A/B testing suggestions**: Generates 3-5 title variations ranked by predicted CTR
- **Primary + secondary keyword placement**: Strategically positions high-intent keywords in first 60 characters
- **Readability scoring**: Ensures titles remain compelling to human readers, not just algorithms
- **Mobile optimization**: Tests title truncation on mobile search results

**Output Example:**
```
Original: "Blue Ceramic Mug"
Optimized Title 1: "Handmade Ceramic Coffee Mug | Blue Artisan Pottery | 12oz"
Optimized Title 2: "Personalized Ceramic Mug | Handmade Blue Coffee Cup | Gift"
Optimized Title 3: "Blue Ceramic Mug Handmade | Coffee Lover Gift | Pottery"
Predicted CTR Improvement: +34%, +28%, +22% respectively
```

### 3. Tag Strategy Optimization
- **All 13 tags filled**: Generates complete tag sets (Etsy allows 13 tags per listing)
- **Tag weighting algorithm**: Places highest-volume, lowest-competition keywords in positions 1-4
- **Synonym expansion**: Includes singular/plural, hyphenated, and related term variations
- **Misspelling capture**: Identifies common misspellings users search for (e.g., "mug" vs "muge")
- **Competitor tag analysis**: Shows which tags top competitors use (and their ranking impact)

**Output Example:**
```
Recommended 13-Tag Set (Priority Order):
1. ceramic mug (18,000 monthly searches, 4.2 competition score)
2. handmade mug (12,500 monthly searches, 3.8 competition score)
3. coffee mug (15,800 monthly searches, 5.1 competition score)
4. personalized mug (8,900 monthly searches, 3.2 competition score)
5-13. [Additional tags with metrics]
Removed Tags: "blue" (too generic), "gift" (oversaturated)
```

### 4. Description Rewriting
- **Scannable structure**: Reformats descriptions with bullet points, headers, and white space for 60% better readability
- **Benefit-focused copy**: Rewrites features as customer benefits ("Hand-thrown" → "Unique heirloom-quality piece you'll treasure for decades")
- **Keyword integration**: Naturally incorporates 8-12 target keywords without keyword stuffing
- **FAQ section generation**: Adds anticipated questions (care instructions, sizing, shipping) that boost dwell time
- **Trust-building elements**: Adds certifications, materials sourcing, and artisan credentials

**Output Example:**
```
ORIGINAL:
"A beautiful blue ceramic mug made by hand. Great for coffee or tea."

OPTIMIZED:
HANDCRAFTED CERAMIC COFFEE MUG | Artisan Blue Pottery

✨ Why You'll Love This Mug:
• Hand-thrown ceramic construction (no two are identical)
• Smooth, chip-resistant glaze perfect for daily use
• Holds 12oz—ideal for coffee, tea, or hot chocolate
• Microwave & dishwasher safe (top rack recommended)

🎁 Perfect Gift For:
Coffee enthusiasts • Tea lovers • Housewarming gifts • Personalization available

📦 Materials & Care:
Kiln-fired stoneware with food-safe glaze. Handmade in Portland, Oregon.
```

### 5. Competitor Analysis Dashboard
- **Top 10 competitor tracking**: Monitors 10 competing listings weekly
- **Ranking position correlation**: Shows which listing elements correlate with top search positions
- **Price sensitivity analysis**: Compares your pricing against competitor positioning
- **Review sentiment analysis**: Extracts keywords from 100+ competitor reviews to identify customer pain points
- **Visual asset comparison**: Analyzes competitor photo styles, count, and composition

---

## Configuration

### Required Environment Variables

```bash
# Etsy API Authentication
ETSY_API_KEY="your_etsy_api_key_here"
ETSY_SHOP_ID="your_shop_id_here"

# Google Trends & Keyword Research
GOOGLE_TRENDS_API_KEY="your_google_api_key"

# Optional: Advanced Features
SIMILARWEB_API_KEY="optional_for_competitor_analysis"
SLACK_WEBHOOK_URL="optional_for_report_notifications"
GOOGLE_SHEETS_API_KEY="optional_for_spreadsheet_exports"
```

### Setup Instructions

1. **Get Etsy API Access:**
   - Visit https://www.etsy.com/developers
   - Create a new app and generate API keys
   - Grant permissions: `listings_r`, `listings_w`, `shops_r`

2. **Enable Google Trends API:**
   - Go to https://console.cloud.google.com
   - Create a new project
   - Enable Trends API and generate OAuth credentials

3. **Optional Slack Integration:**
   - Create a Slack webhook at https://api.slack.com/apps
   - Paste webhook URL into `SLACK_WEBHOOK_URL`

4. **Verify Configuration:**
   ```
   Test my Etsy API connection
   Show: Shop name, active listing count, last 30 days performance
   ```

---

## Example Outputs

### Output 1: Full Listing Optimization Report

```
LISTING OPTIMIZATION REPORT
Generated: January 15, 2025

CURRENT PERFORMANCE:
• Search Impressions (30-day): 245
• Click-Through Rate: 2.1%
• Conversion Rate: 1.8%
• Revenue Impact: $180

OPTIMIZED PROJECTIONS (90-day):
• Estimated Impressions: +156% (639)
• Projected CTR: +45% (3.05%)
• Projected Conversion: +22% (2.2%)
• Revenue Impact: $612 (+240%)

TITLE OPTIMIZATION:
Current: "Blue Ceramic Mug"
Recommended: "Handmade Ceramic Coffee Mug | Blue Artisan Pottery | 12oz"
Improvement: +34% predicted CTR

TAG OPTIMIZATION:
Removed: "blue" (too generic), "gift" (oversaturated)
Added: "personalized mug", "ceramic coffee cup", "handmade pottery"
Competitive Advantage: 7 new keywords with <3.5 competition score

DESCRIPTION REWRITE:
Original Length: 45 words
Optimized Length: 180 words (optimal for dwell time)
Keyword Integration: 11 target keywords (natural placement)
Readability Score: 8.2/10

COMPETITOR BENCHMARKING:
Your Current Position: #47 for "ceramic mug"
Top Competitor: #3 (Title length: 58 chars, Tags: ceramic, mug, handmade...)
Gap Analysis: Missing "personalized" angle, underutilizing long-tail keywords
```

### Output 2: Batch Optimization Spreadsheet

| Product | Current Title | Optimized Title | Tag Gap | Est. Revenue Impact | Priority |
|---------|---------------|-----------------|---------|---------------------|----------|
| Blue Mug | Blue Ceramic Mug | Handmade Ceramic Coffee Mug \| Blue Artisan Pottery | +5 tags | +$180/mo | HIGH |
| Wooden Box | Wood Box Storage | Personalized Wooden Box \| Rustic Storage \| Handmade Gift | +3 tags | +$95/mo | MEDIUM |
| Scarf | Winter Scarf | Chunky Knit Scarf \| Handmade Winter \| Cozy Gift | +4 tags | +$240/mo | HIGH |

---

## Tips & Best Practices

### 1. Timing Your Optimizations
- **Launch on Tuesdays-Thursdays** for maximum visibility in Etsy's algorithm (weekend traffic peaks)
- **Seasonal updates**: Refresh tags 60 days before major shopping seasons (holiday, Mother's Day, back-to-school)
- **Test one variable at a time**: Change title, wait 2 weeks, then update tags. This isolates what drives results.

### 2. Keyword Research Strategy
- **Start with your best sellers**: Optimize top 10% of listings first for fastest ROI
- **Use long-tail keywords**: "Handmade ceramic coffee mug for coffee lovers" (lower competition, higher intent)
- **Monitor seasonal trends**: Use Google Trends to catch rising keywords 30 days before peak demand
- **Analyze customer language**: Read your own reviews—customers use different words than competitors' descriptions

### 3. Title Crafting Rules
- **Lead with primary keyword**: "Ceramic Mug" not "Beautiful Handmade Ceramic Mug"
- **Include benefit in title**: "Personalized" or "Handmade" increases CTR by 15-25%
- **Stay under 60 characters for mobile**: First 60 characters are all users see on mobile search
- **Avoid keyword stuffing**: Maximum 2-3 keywords per title (Etsy penalizes over-optimization)

### 4. Tag Optimization Tactics
- **Fill all 13 tags**: Empty slots are wasted ranking opportunities
- **Mix search volumes**: 3 high-volume (5k+ searches), 5 medium (1k-5k), 5 long-tail (<1k)
- **Test tag order**: Your top 4 tags have 40% more weight—place your best keywords there
- **Update quarterly**: Seasonal keywords shift; refresh tags every 90 days

### 5. Description Best Practices
- **Scannable format**: 70% of users skim—use headers, bullets, short paragraphs
- **Answer FAQs early**: Size, care instructions, shipping time in first 3 paragraphs
- **Include trust signals**: "Handmade in [location]", "5-star rated", "Ships within 48 hours"
- **Call-to-action**: End with urgency ("Only 3 in stock") or personalization offer

### 6. A/B Testing Framework
```
Week 1-2: Deploy optimized title
Track: Impressions, CTR, conversion rate
Week 3-4: Deploy optimized tags
Track: Search position change, CTR improvement
Week 5-6: Deploy optimized description
Track: Conversion rate, average order value
```

---

## Safety & Guardrails

### What This Skill Will NOT Do

- **Violate Etsy ToS**: This skill respects Etsy's policies. It will not:
  - Generate misleading or false product claims
  - Use competitor brand names as keywords (trademark violation)
  - Implement keyword stuffing or cloaking techniques
  - Scrape competitor listings without permission
  - Create duplicate listings or content across multiple shops

- **Guarantee specific rankings**: SEO is probabilistic. This skill provides data-driven recommendations but cannot guarantee #1 search position. Algorithm changes, competitor actions, and market conditions affect results.

- **Manipulate reviews or ratings**: This skill analyzes existing reviews only; it will not generate fake reviews, incentivize reviews, or manipulate ratings.

- **Access private shop data**: This skill requires explicit API permissions. It will not access competitor shop analytics without authorization.

- **Recommend unethical pricing**: This skill provides competitive analysis but will not recommend predatory pricing or price-fixing strategies.

### Limitations

- **Etsy API rate limits**: Free tier allows 10 requests/minute. Batch optimizations may take 2-3 hours for 100+ listings.
- **Keyword data freshness**: Google Trends data updates weekly; real-time keyword volume is estimated based on Etsy search patterns.
- **Language support**: Currently optimized for English-language listings. Non-English listings require manual review.
- **New shops**: Shops with <10 sales may see slower ranking improvements (Etsy prioritizes established sellers).
- **Niche products**: Products with <100 monthly searches may not have sufficient keyword data for optimization.

---

## Troubleshooting

### FAQ & Common Issues

**Q: I optimized my listing but saw no improvement in 2 weeks. What's wrong?**

A: Etsy's algorithm takes 2-4 weeks to re-rank listings after changes. Common issues:
- You changed multiple elements at once (test one variable)
- Your keywords are too competitive (try long-tail variants)
- Your listing photos are low-quality (images matter more than text)
- Your shop has low reviews (focus on getting 5-star reviews first)

**Action**: Wait 4 weeks, then check analytics. If no improvement, try different keywords or consider lowering price by 5-10%.

---

**Q: The tool says my keyword has "high competition" but I want to rank for it. What do I do?**

A: High-competition keywords are hard to rank for quickly. Strategy:
1. **Layer with long-tail**: Instead of "ceramic mug", target "handmade ceramic mug for coffee lovers"
2. **Compete on reviews**: Get 50+ 5-star reviews, then compete on popular keywords
3. **Use in description only**: Put competitive keywords in description body (not title/tags) while building authority
4. **Create content**: Write a blog post about the keyword (impro