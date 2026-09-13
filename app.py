from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Program Delivery Dashboard", page_icon="🤖", layout="wide")

DATA = Path(__file__).parent / "data" / "ai_programs.csv"
df = pd.read_csv(DATA)

st.title("AI Program Delivery Dashboard")
st.caption("Executive portfolio view for AI / GenAI program delivery")

budget = df["budget_usd"].sum()
actual = df["actual_usd"].sum()
variance = actual - budget
milestones = df["milestones_total"].sum()
on_time = df["milestones_on_time"].sum()
on_time_pct = (on_time / milestones) * 100
high_risks = df["high_risks"].sum()
dependencies = df["critical_dependencies"].sum()

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Portfolio Budget", f"${budget/1_000_000:.1f}M")
c2.metric("Budget Variance", f"${variance/1_000:.0f}K", delta=f"{variance/budget*100:.1f}%")
c3.metric("Milestones On Time", f"{on_time_pct:.1f}%")
c4.metric("High Risks", int(high_risks))
c5.metric("Critical Dependencies", int(dependencies))

st.divider()

left, right = st.columns([1.3, 1])
with left:
    st.subheader("Program Health")
    health = df[["program", "status", "value_score", "high_risks", "critical_dependencies"]].copy()
    st.dataframe(health, use_container_width=True, hide_index=True)

with right:
    st.subheader("Portfolio Status")
    st.bar_chart(df.set_index("program")["value_score"], use_container_width=True)

st.subheader("Budget vs. Actual")
finance = df.set_index("program")[["budget_usd", "actual_usd"]]
st.bar_chart(finance, use_container_width=True)

st.subheader("Program Detail")
selected = st.selectbox("Select a program", df["program"].tolist())
row = df[df["program"] == selected].iloc[0]

p1, p2, p3, p4 = st.columns(4)
p1.metric("Status", row["status"])
p2.metric("Value Score", f"{row['value_score']}/100")
p3.metric("High Risks", int(row["high_risks"]))
p4.metric("Critical Dependencies", int(row["critical_dependencies"]))

st.progress(min(float(row["milestones_on_time"] / row["milestones_total"]), 1.0), text="Milestone completion quality")

st.info("Portfolio demonstration using synthetic sample data. No confidential employer or client information is included.")
