# Data Analysis Report 📈

A Python script that analyzes 28 days of SMP member fitness data using Pandas and NumPy — producing a structured weekly and monthly report.

---

## What It Does

Loads 28 days of fitness logs into a DataFrame and outputs:

- **Overall metrics** — total steps, averages, 10K hit rate, sleep, bench press range and trend
- **Weekly breakdown** — per-week averages for steps and bench press, plus 10K+ day counts
- **Protocol comparison** — average steps, sleep, and bench press grouped by OMAD vs 2MAD
- **Top 3 step days** — best performances with their protocols

---

## Why It Exists

Raw fitness logs are hard to interpret without structure. This project turns 28 days of numbers into something you can actually read:

- **Weekly trends** — see if you're improving or plateauing
- **Protocol comparison** — does OMAD outperform 2MAD on your metrics?
- **Clean output** — formatted terminal report, no notebooks, no charts to squint at
- **Pandas fundamentals** — loading, grouping, filtering, aggregating, and reporting in one place

Built as a practical exercise in data analysis: real structure, real questions, real answers.

---

## How to Run It

```bash
pip install pandas numpy

python data_analysis_report.py
