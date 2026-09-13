# AI Program Delivery Dashboard

A recruiter-facing portfolio project showing how a **Technical Program Manager / AI Program Manager** can govern multiple AI initiatives from intake through production.

![AI Program Delivery Dashboard](assets/dashboard_preview.svg)

## Executive View

This project converts AI delivery data into a leadership-level view of:

- Portfolio budget and variance
- Milestone performance
- Program health
- High-severity risks
- Critical dependencies
- Business value scores
- Launch readiness

The sample dashboard currently shows a **$4.95M AI portfolio**, **88.1% on-time milestone performance**, **9 high risks**, and **14 critical dependencies** across four illustrative programs.

> All data in this repository is synthetic sample data. No confidential employer or client information is included.

## Interactive Dashboard

The repository now includes a runnable **Streamlit executive dashboard**.

### Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app provides:

- Executive KPI cards
- Portfolio health table
- Value score visualization
- Budget vs. actual comparison
- Program-level drilldown
- Milestone delivery indicator

## Business Problem

AI programs often span engineering, data, security, legal, product, infrastructure, and operations. Leadership needs a single view of delivery health, risk, dependencies, financial performance, and business value.

A Technical Program Manager must make that complexity understandable enough for leaders to make decisions quickly.

## What This Project Demonstrates

- AI / GenAI program governance
- Program intake and prioritization
- Milestone and dependency management
- Executive KPI design
- Budget and forecast monitoring
- AI-specific risk and readiness checkpoints
- Delivery health scoring
- Value-realization tracking
- Cross-functional launch readiness

## Portfolio Programs

The synthetic portfolio includes:

1. **GenAI Knowledge Assistant** — Green
2. **Predictive Maintenance AI** — Amber
3. **AI Service Agent** — Green
4. **Document Intelligence** — Red

This makes it easy to demonstrate how a TPM identifies programs requiring executive intervention rather than treating every initiative equally.

## Repository Structure

- `app.py` — interactive Streamlit executive dashboard
- `requirements.txt` — Python dependencies
- `assets/dashboard_preview.svg` — recruiter-facing dashboard visual
- `data/ai_programs.csv` — sample portfolio data
- `src/dashboard_metrics.py` — KPI calculations
- `governance/launch_readiness_checklist.md` — AI launch-readiness framework
- `governance/risk_register_template.csv` — reusable program risk register

## Sample KPIs

- Portfolio budget variance
- % milestones delivered on time
- Critical dependency count
- Open high-severity risks
- Production-readiness status
- Business value score
- Model / solution reliability readiness

## Why This Matters for Technical Program Management

The value of a TPM is not simply maintaining schedules. It is creating enough structure across engineering, product, security, data, finance, and operations that teams can deliver reliably and leadership can make informed decisions.

This project demonstrates that operating model in a simple, inspectable format.

---

**Emmanuel Edore**  
Technical Program Management | AI & Digital Transformation | PMO | Cybersecurity | Cloud | Salesforce
