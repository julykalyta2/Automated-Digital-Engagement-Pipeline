from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(BASE / "data/sample_engagement.csv", parse_dates=["date"])
df["engagements"] = df[["likes", "comments", "shares", "saves"]].sum(axis=1)
df["engagement_rate_pct"] = (100 * df["engagements"] / df["reach"]).round(2)
# Illustrative anomaly rule: reach more than 1.75x platform median.
platform_median = df.groupby("platform")["reach"].transform("median")
df["high_reach_flag"] = df["reach"] > 1.75 * platform_median
df.to_csv(OUT / "post_performance.csv", index=False)
summary = df.groupby("platform").agg(posts=("post_id", "count"), total_reach=("reach", "sum"), avg_engagement_rate_pct=("engagement_rate_pct", "mean"), link_clicks=("link_clicks", "sum")).round(2)
summary.to_csv(OUT / "platform_summary.csv")
top = df.sort_values("engagement_rate_pct", ascending=False).head(10)
top.to_csv(OUT / "top_posts.csv", index=False)
flags = df.loc[df["high_reach_flag"]].sort_values("reach", ascending=False)
flags.to_csv(OUT / "reach_anomalies.csv", index=False)
fig, ax = plt.subplots(figsize=(8, 4.5))
summary["avg_engagement_rate_pct"].plot(kind="bar", ax=ax)
ax.set(title="Average Engagement Rate by Platform (Synthetic Data)", ylabel="Engagement rate (%)", xlabel="")
ax.tick_params(axis="x", rotation=0)
fig.tight_layout()
fig.savefig(OUT / "engagement_comparison.png", dpi=170)
plt.close(fig)
report = f"""# Automated Engagement Performance Brief

**Demo only:** 90 synthetic posts. No real Meta account data or API access.

## Platform performance
{summary.to_markdown()}

## High-reach anomalies
{len(flags)} posts exceeded 1.75x their platform's median reach. This is a simple demonstration threshold, not a production statistical model.

## Top-performing example
Post {top.iloc[0]['post_id']} ({top.iloc[0]['platform']}, {top.iloc[0]['topic']}) had a {top.iloc[0]['engagement_rate_pct']:.2f}% engagement rate.

## Suggested actions
- Review the format and topic of top-performing posts.
- Test two posting windows and compare results.
- Use human review before scheduling any AI-assisted content.
- Connect approved Meta APIs or export files for live reporting in a future version.

## Measurement disclaimer
No live posts were scheduled, no actual platform automation was deployed, and no time savings or consistency rate has been measured.
"""
(OUT / "performance_brief.md").write_text(report, encoding="utf-8")
print("Created engagement analytics, anomaly flags, chart, and performance brief.")
