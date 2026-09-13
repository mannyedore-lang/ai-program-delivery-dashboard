import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "ai_programs.csv"

def load_programs():
    with DATA.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def summarize(rows):
    total_budget = sum(float(r["budget_usd"]) for r in rows)
    total_actual = sum(float(r["actual_usd"]) for r in rows)
    total_milestones = sum(int(r["milestones_total"]) for r in rows)
    on_time = sum(int(r["milestones_on_time"]) for r in rows)
    high_risks = sum(int(r["high_risks"]) for r in rows)
    dependencies = sum(int(r["critical_dependencies"]) for r in rows)

    return {
        "portfolio_budget_usd": round(total_budget, 2),
        "portfolio_actual_usd": round(total_actual, 2),
        "budget_variance_usd": round(total_actual - total_budget, 2),
        "milestone_on_time_pct": round((on_time / total_milestones) * 100, 1),
        "open_high_risks": high_risks,
        "critical_dependencies": dependencies,
    }

if __name__ == "__main__":
    metrics = summarize(load_programs())
    for k, v in metrics.items():
        print(f"{k}: {v}")
