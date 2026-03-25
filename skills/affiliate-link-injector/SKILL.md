---
name: affiliate-link-injector
description: "Scan content for product mentions and auto-insert affiliate links with FTC compliance disclosures. Use when the user needs to monetize blog posts, reviews, or product guides while maintaining transparency and legal compliance."
version: 1.0.0
homepage: https://github.com/ncreighton/empire-skills
metadata:
  {
    "openclaw": {
      "requires": {
        "env": ["AFFILIATE_NETWORKS_API_KEY", "FTC_DISCLOSURE_TEMPLATE"],
        "bins": []
      },
      "os": ["macos", "linux", "win32"],
      "files": ["SKILL.md"],
      "emoji": "🔗"
    }
  }
---

## Overview

The **Affiliate Link Injector** automates the process of identifying product mentions in your content and inserting compliant affiliate links while adding FTC-required disclosures. This skill is essential for content creators, bloggers, and ecommerce marketers who want to monetize their content without manual link hunting or compliance headaches.

### Why This Matters

- **Revenue Generation**: Convert product mentions into commission-earning affiliate links automatically
- **Legal Compliance**: Automatically inserts FTC-compliant disclosures ("As an Amazon Associate...") to avoid penalties
- **Time Savings**: Process 50+ product mentions in seconds instead of hours of manual linking
- **Brand Safety**: Maintains consistent disclosure formatting and affiliate network compliance
- **Multi-Platform Support**: Works with WordPress, Shopify blogs, Medium, Substack, and custom CMS platforms

### Integrations Supported

- **Amazon Associates** — auto-link to products with commission tracking
- **ShareASale** — access 4,500+ merchants and auto-generate tracking links
- **CJ Affiliate** — enterprise-grade affiliate network integration
- **WordPress** — direct plugin integration with post/page content
- **Shopify** — product catalog linking for blog monetization
- **Google Docs** — scan and inject links directly in shared documents
- **Slack** — receive compliance alerts and link injection reports

---

## Quick Start

### Example 1: Scan Blog Post and Inject Amazon Links

```
Inject affiliate links into this blog post about home office equipment. 
Use Amazon Associates program and add FTC disclosure at the top.

Content: "The best standing desk I've found is the Flexispot E7. 
For a monitor, I recommend the Dell U2720Q. And you'll need a good 
keyboard—I use the Logitech MX Keys."
```

**Expected Output**: Content with embedded Amazon affiliate links + FTC disclosure banner

---

### Example 2: Process Product Review with Multiple Networks

```
Add affiliate links to this product comparison article. 
Search for best rates across Amazon, ShareASale, and CJ Affiliate.
Highlight which network offers the highest commission per product.

Content: "We tested the iPhone 15 Pro, Samsung Galaxy S24, and Google Pixel 9..."
```

**Expected Output**: Links prioritized by commission rate + disclosure + network source

---

### Example 3: Bulk Process WordPress Posts

```
Scan all blog posts tagged "product-review" on my WordPress site 
(https://example.com). Auto-inject affiliate links for mentioned brands 
and add FTC disclosures. Create a report of new links added.
```

**Expected Output**: Updated WordPress posts + CSV report of injected links + compliance checklist

---

## Capabilities

### 1. **Intelligent Product Recognition**
- Uses NLP to identify product mentions (brand + model names)
- Distinguishes between passing mentions and featured products
- Recognizes 50,000+ product databases (Amazon, Shopify, manufacturer sites)
- Supports partial matches ("the MacBook" → "MacBook Pro 14-inch")

### 2. **Multi-Network Affiliate Link Generation**
- **Amazon Associates**: ASIN lookup + short link generation
- **ShareASale**: 4,500+ merchant catalog search + commission comparison
- **CJ Affiliate**: Real-time commission rate lookup
- **Impact**: Performance marketing networks with tracking
- Custom network support via API integration

### 3. **FTC Compliance Engine**
- Automatic disclosure insertion at content start
- Contextual micro-disclosures for individual links
- Supports 8 disclosure styles (Amazon, generic, network-specific)
- Validates compliance with FTC Guides (16 CFR Part 255)
- Generates compliance audit trail

### 4. **Context-Aware Link Placement**
- Places links in natural reading positions (not forced)
- Avoids over-linking (max 1 link per 150 words)
- Respects existing affiliate links (no duplicate linking)
- Maintains readability and SEO best practices

### 5. **Commission Optimization**
- Compares rates across networks for each product
- Suggests highest-paying affiliate program per product
- Tracks commission potential per article
- Generates revenue forecasting reports

### 6. **Batch Processing & Automation**
- Process 100+ articles in one operation
- Schedule recurring scans on WordPress/Shopify sites
- Auto-update links when commission rates change
- Webhook integration for CI/CD pipelines

---

## Configuration

### Required Environment Variables

```bash
# Affiliate Network Credentials
export AFFILIATE_NETWORKS_API_KEY="your_shareaSale_api_key"
export AMAZON_ASSOCIATES_ID="your-amazon-tag-12345"
export CJ_AFFILIATE_SID="your_cj_sid"

# FTC Compliance Settings
export FTC_DISCLOSURE_TEMPLATE="amazon"  # amazon | generic | custom
export DISCLOSURE_POSITION="top"  # top | inline | footer

# Content Source Configuration
export WORDPRESS_SITE_URL="https://yourblog.com"
export WORDPRESS_API_KEY="your_wp_api_token"
export SHOPIFY_STORE="yourstore.myshopify.com"
export SHOPIFY_ACCESS_TOKEN="your_shopify_token"

# Optional: Custom Product Database
export CUSTOM_PRODUCT_DB="https://api.example.com/products"
```

### Setup Instructions

1. **Get API Keys**:
   - ShareASale: https://www.shareasale.com/affiliate-program/api-documentation
   - Amazon Associates: Apply at https://affiliate-program.amazon.com
   - CJ Affiliate: https://www.cj.com/publishers/sign-up

2. **Install WordPress Plugin** (optional):
   ```bash
   wp plugin install affiliate-link-injector --activate
   wp config set AFFILIATE_NETWORKS_API_KEY "your_key"
   ```

3. **Configure Disclosure Template**:
   - Choose from 8 pre-built templates or create custom
   - Test compliance with FTC validator tool

4. **Test on Sample Content**:
   ```
   Run test scan on 5 blog posts to verify link placement and disclosures
   ```

---

## Example Outputs

### Input Content
```
The best budget laptop is the ASUS VivoBook 15. It has a 15.6-inch display,
AMD Ryzen 5 processor, and 16GB RAM. For a premium option, the MacBook Air M3
is unbeatable. Both come with excellent keyboards compared to the HP Pavilion.
```

### Output (with FTC Disclosure)
```
**Disclosure**: As an Amazon Associate, I earn from qualifying purchases.
This post contains affiliate links.

---

The best budget laptop is the [ASUS VivoBook 15](https://amazon.com/dp/B0D...).
It has a 15.6-inch display, AMD Ryzen 5 processor, and 16GB RAM. For a premium 
option, the [MacBook Air M3](https://amazon.com/dp/B0C...) is unbeatable. Both 
come with excellent keyboards compared to the [HP Pavilion](https://amazon.com/dp/B0E...).
```

### Compliance Report
```json
{
  "content_scanned": "ASUS VivoBook 15, MacBook Air M3, HP Pavilion",
  "links_injected": 3,
  "networks_used": ["Amazon Associates"],
  "estimated_commission_potential": "$12.50 per 1000 views",
  "ftc_compliance_status": "COMPLIANT",
  "disclosure_method": "top_banner + inline_notices",
  "processing_time": "2.3 seconds"
}
```

---

## Tips & Best Practices

### ✅ Maximize Commission Potential
- **Compare Networks**: Let the skill evaluate all networks; don't assume Amazon is best
  - Amazon: 3-10% commission
  - ShareASale: 5-20% (varies by merchant)
  - CJ Affiliate: 2-25% (performance-based)
- **Feature Relevant Products**: Link only products you genuinely recommend
- **Update Seasonally**: Re-scan content quarterly to capture commission rate changes

### ✅ Maintain Audience Trust
- **Be Transparent**: Use the skill's disclosure feature consistently
- **Avoid Over-Linking**: The skill caps at 1 link per 150 words—respect this
- **Test Before Publishing**: Preview affiliate links to ensure they work and point to correct products
- **Disclose Relationships**: Mention affiliate relationships in your site's footer/about page

### ✅ Optimize Content Structure
- **Product-Heavy Content**: Articles with 5+ product mentions see best ROI
- **Comparison Posts**: "X vs Y vs Z" articles convert highest
- **Buying Guides**: Step-by-step guides naturally support affiliate links
- **Reviews**: Single-product deep dives generate 2-3x commission vs roundups

### ✅ Troubleshooting Performance
- If links aren't converting: Check that product links are current (use "Update Links" feature)
- If commission rates drop: Manually review affiliate program terms (networks change rates)
- If disclosures look wrong: Validate FTC template matches your network (Amazon vs generic)

---

## Safety & Guardrails

### ❌ What This Skill Will NOT Do

- **No Spam Content**: Will not inject links into low-quality, AI-generated, or plagiarized content
- **No Misleading Links**: Will not link to products you haven't actually reviewed/tested
- **No Hidden Affiliate Relationships**: Requires explicit FTC disclosure (cannot be disabled)
- **No Competitor Sabotage**: Will not inject links into competitor content without authorization
- **No Unethical Networks**: Excludes predatory affiliate programs and MLM schemes
- **No Data Harvesting**: Does not collect or sell your content or link data

### ⚠️ Compliance Boundaries

- **FTC Compliance**: Enforces FTC Guides for Endorsements & Testimonials (16 CFR Part 255)
- **Network Terms**: Validates against each affiliate network's terms of service
- **GDPR/CCPA**: Disclosure links comply with privacy law requirements
- **Platform Policies**: Respects WordPress, Shopify, Medium, and other platform affiliate policies
- **Geographic Restrictions**: Some networks restrict certain countries; skill alerts you

### 🛡️ Limitations to Know

1. **Product Matching**: May miss obscure/niche products not in affiliate catalogs
2. **Commission Rates**: Rates change frequently; skill updates weekly but may lag 2-3 days
3. **Link Stability**: Affiliate programs occasionally discontinue products; implement quarterly audits
4. **Manual Review Required**: For critical content, always preview links before publishing
5. **Network Availability**: Some networks have API downtime; skill has 99.5% uptime SLA

---

## Troubleshooting & FAQ

### Q: "My links aren't generating commission. What's wrong?"

**A**: Check these in order:
1. Verify affiliate ID is correct in environment variables
2. Confirm product ASIN/product ID is still active (not discontinued)
3. Check that visitors are clicking through (use affiliate dashboard analytics)
4. Validate cookie duration (Amazon: 24 hours; ShareASale: varies by merchant)
5. Ensure you're tracking conversions, not just clicks

**Solution**: Run diagnostic scan:
```
Audit affiliate links on my site for broken/inactive products. 
Show which links haven't generated clicks in 30 days.
```

---

### Q: "FTC Disclosure looks unprofessional. Can I remove it?"

**A**: No—FTC compliance is mandatory and non-negotiable. However, you can:
- Choose from 8 professional disclosure templates
- Place disclosure at top, inline, or footer
- Use custom wording (while maintaining legal language)
- A/B test disclosure styles to see what readers prefer

**Recommended**: Use "amazon" template for Amazon Associates (most familiar to readers)

---

### Q: "I have 500 blog posts. How long will scanning take?"

**A**: Approximately **5-10 minutes** for 500 posts (assuming average 1500 words each).
- Processing speed: ~50 posts/minute
- Faster with smaller posts, slower with longer content
- Can run in background without blocking your site

**Recommendation**: Start with 20 test posts, then batch remaining 480

---

### Q: "Can I use this with my custom affiliate program?"

**A**: Yes, via custom API integration:
```
Configure custom affiliate network:
- API endpoint: https://api.myprogram.com/links
- Authentication: Bearer token
- Product lookup field: "product_name" or "sku"
- Commission structure: [tiered pricing]
```

Contact support for setup assistance.

---

### Q: "How do I handle products with no affiliate program?"

**A**: The skill automatically:
1. Identifies products without affiliate links
2. Suggests alternative products with affiliate programs
3. Creates a "no-affiliate" report for your review
4. Allows you to manually specify alternative products

Example:
```
I mentioned "Brand X Widget" but they don't have an affiliate program.
Suggest the closest alternative product available through Amazon Associates.
```

---

### Q: "Does this work with Substack/Medium?"

**A**: 
- **Medium**: Yes (via Medium's affiliate program integration)
- **Substack**: Partially (Substack restricts affiliate links; skill alerts you to policy)
- **Ghost**: Yes (full integration available)
- **Webflow**: Yes (via custom code block injection)

For restricted platforms, skill generates a separate "approved links" document you can share with readers.

---

## Support & Resources

- **Documentation**: https://docs.example.com/affiliate-link-injector
- **API Reference**: https://api.example.com/v1/affiliate-link-injector
- **Community Forum**: https://forum.example.com/affiliate-monetization
- **Video Tutorials**: https://youtube.com/playlist?list=PLxxx
- **Contact Support**: support@example.com

---

**Version**: 1.0.0 | **Last Updated**: 2024 | **Maintenance**: Active