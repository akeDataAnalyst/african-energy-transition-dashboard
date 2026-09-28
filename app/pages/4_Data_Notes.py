import streamlit as st

# Sidebar Global Controls
st.sidebar.title("Energy Transition Intel")
st.sidebar.markdown("---")
cohort_countries = ["Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda", "Ghana", "Nigeria", "South Africa", "Egypt", "Morocco"]
st.sidebar.selectbox("Global Country Focus", cohort_countries, key="selected_country")
st.sidebar.markdown("---")

st.title("Data Notes & Methodology")
st.markdown("""
#### Data Sources & Architecture
- **Ember Yearly Electricity Data:** Tracks global electricity generation, capacity, emissions, and demand from 1985 to recent years.
- **World Bank World Development Indicators (WDI):** Provides longitudinal tracking of electricity access rates.
- **DuckDB Analytical Database:** High-performance embedded SQL database powering instantaneous cross-filtering and metric calculations.
- **Streamlit & Plotly:** Frontend reactive interface and interactive visualizations.

#### Target Cohort
Ethiopia, Kenya, Tanzania, Uganda, Rwanda, Ghana, Nigeria, South Africa, Egypt, and Morocco.
""")