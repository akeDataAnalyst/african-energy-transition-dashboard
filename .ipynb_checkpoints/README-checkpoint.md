# African Electricity Transition Intelligence Dashboard

> An evidence-based, multi-page analytics platform tracking power generation mixes, renewable energy integration, grid access electrification, and decarbonization pathways across 10 strategic African nations.

---

## Project Overview
As Africa navigates rapid economic growth and urbanization, understanding the structural shifts in its power systems is critical. This project delivers a production-grade analytics platform built to monitor, benchmark, and visualize the electricity transition trajectory of 10 key African economies (Ethiopia, Kenya, Tanzania, Uganda, Rwanda, Ghana, Nigeria, South Africa, Egypt, and Morocco). 

The platform bridges raw energy data and executive-level intelligence through a high-performance embedded analytical database and an interactive Streamlit web application.

---

## The Problem
* **Data Fragmentation:** Energy transition data is often locked across disparate global repositories (such as Ember's multi-decade generation tracking and World Bank development indicators), making cross-national benchmarking slow and tedious.
* **Lack of Granularity:** High-level continental summaries frequently obscure national nuances—such as Ethiopia's nearly 100% renewable hydro-dominant grid versus fossil-heavy industrial baseloads in other regions.
* **Actionable Insight Gaps:** Stakeholders require clean, instantaneous visualizations to evaluate decarbonization progress, renewable penetration, and electricity access deficits without complex data engineering overhead.

---

## The Solution
I engineered an end-to-end data pipeline and interactive multi-page intelligence platform:
1. **Automated Data Ingestion & Cleaning:** Standardized country nomenclature and melted longitudinal indicators into analysis-ready formats.
2. **Embedded Analytical Database:** Centralized historical records into DuckDB for instantaneous, memory-efficient SQL queries.
3. **Modular Backend Engine:** Built reusable Python helper modules (`src/metrics.py`) to compute core metrics like clean energy shares, technology breakdowns, and socioeconomic access rates.
4. **Interactive Multi-Page Streamlit Frontend:** Deployed a reactive web application featuring global persistent controls, deep-dive technology charts, and regional cohort benchmarks.

---

## Tech Stack

* **Programming Language:** Python 3.10+
* **Data Processing & Analysis:** Pandas, NumPy
* **Analytical Database:** DuckDB (Embedded SQL analytics)
* **Web Application Framework:** Streamlit 
* **Data Visualization:** Plotly (Interactive charts, regional bars, and trend lines)
* **Version Control & Environment:** Git

---

## Data Sources

1. **Ember Yearly Electricity Data:** 
   * Tracks global annual electricity generation, capacity, emissions, and demand from 1985 to recent years.
   * Filtered to isolate disaggregated technology sources (Hydro, Solar, Wind, Gas, Coal, Bioenergy, etc.) from aggregate totals.
2. **World Bank World Development Indicators (WDI):**
   * Provides longitudinal tracking of socioeconomic development metrics, specifically Access to Electricity (% of population).

---

## Results & Key Insights

* **Renewable Leaders:** Countries like Ethiopia showcase 100% clean energy generation profiles driven by extensive hydroelectric infrastructure.
* **Fossil & Industrial Hubs:** Nations like Egypt and South Africa highlight complex thermal transitions, balancing heavy natural gas and coal baseloads with rapidly scaling solar and wind investments.
* **Electrifying Access:** Longitudinal tracking via World Bank indicators reveals steady multi-decade improvements in grid penetration across East and West African target hubs.

---

## Project Structure

```text
african-energy-transition-dashboard/
│
├── data/
│   ├── raw/                 
│   ├── processed/
│   └── energy_transition.db 
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_indicator_prototypes.ipynb
│
├── src/
│   ├── ingest.py            
│   └── metrics.py          
│
├── app/
│   ├── app.py               
│   └── pages/              
│       ├── 1_Electricity_Mix.py
│       ├── 2_Access_and_Development.py
│       ├── 3_Regional_Comparison.py
│       └── 4_Data_Notes.py
│
├── requirements.txt         
└── README.md