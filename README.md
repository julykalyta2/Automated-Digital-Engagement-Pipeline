# Automated Digital Engagement & Omnichannel Content Pipeline

**Portfolio demonstration | JK Homes simulated Facebook and Instagram content operations**

A reproducible Python demonstration of **AI-assisted social content planning**, omnichannel engagement analytics, simple anomaly flagging, and draft calendar automation. Uses **synthetic data** and sample AI-assisted copy. No Meta API credentials or paid AI API required.

## What it does
1. Reads 90 simulated Facebook and Instagram posts.
2. Calculates reach, engagement rates, clicks, and per-platform metrics.
3. Flags unusually high reach using a transparent 1.75× platform-median rule.
4. Exports top posts, platform KPI summaries, and a comparison chart.
5. Produces a management performance brief.
6. Generates a **draft** multi-platform content calendar from sample AI-assisted captions.

## Outputs
- [`outputs/performance_brief.md`](outputs/performance_brief.md) — performance insights and recommendations
- [`outputs/engagement_comparison.png`](outputs/engagement_comparison.png) — platform chart
- [`outputs/platform_summary.csv`](outputs/platform_summary.csv) — channel KPIs
- [`outputs/top_posts.csv`](outputs/top_posts.csv) — top engagement rates
- [`outputs/reach_anomalies.csv`](outputs/reach_anomalies.csv) — flagged posts
- [`outputs/sample_content_calendar.csv`](outputs/sample_content_calendar.csv) — draft publishing plan

## Run locally or in Google Colab
```bash
pip install -r requirements.txt
python src/analyze_engagement.py
python src/create_calendar.py
```

## Tech stack
Python, pandas, matplotlib, CSV, GitHub; AI-assisted sample copy is included in `data/ai_content_examples.csv`.

## Example AI workflow
**Prompt template:** "Write a concise, compliant real-estate education caption for [platform] on [topic], with one practical takeaway and a neutral call to action. Avoid unsupported market claims, guarantees, and fair-housing-sensitive targeting. Return draft text for human approval."

**Human-in-the-loop design:** Content examples are drafts only. A human must check accuracy, fair-housing compliance, brokerage advertising rules, and approval before publishing.

## Limitations and honest disclosure
- **All engagement data is synthetic**; no real Meta Business Suite account was connected.
- Sample captions are illustrative AI-assisted content examples, not proof of an automated LLM API integration.
- **No automatic publishing** has been performed.
- The anomaly detector is a rule-based threshold, not an ML model.
- No measured productivity gain or 100% consistency claim is made.

## Future improvements
Add a permitted Meta data export or API connection, LLM-assisted caption generation, approval workflow, scheduling integration, and measured operational reliability.

## Resume-ready summary
**Automated Digital Engagement & Omnichannel Content Pipeline — Portfolio Project**
- Developed a Python demonstration analyzing 90 synthetic Facebook and Instagram posts, including engagement KPIs, channel comparisons, and anomaly flags.
- Built automated exports for top-performing content, performance reporting, and a draft omnichannel content calendar.
- Documented an AI-assisted content workflow with human review and clear limitations for simulated data and non-live integrations.
