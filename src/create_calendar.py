from pathlib import Path
import pandas as pd
BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)
drafts = pd.read_csv(BASE / "data/ai_content_examples.csv")
dates = pd.date_range("2026-11-02", periods=12, freq="2D")
rows = []
for i, date in enumerate(dates):
    item = drafts.iloc[i % len(drafts)]
    rows.append({"scheduled_date_example": date.date().isoformat(), "platform": item["platform"], "topic": item["topic"], "content_format": item["content_format"], "draft_caption": item["ai_assisted_draft"], "status": "Draft - human approval required", "published": False})
pd.DataFrame(rows).to_csv(OUT / "sample_content_calendar.csv", index=False)
print("Created draft content calendar (not published or connected to Meta).")
