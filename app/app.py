"""
African Electricity Transition Intelligence Dashboard.
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.metrics import get_country_summary
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="African Electricity Transition Intelligence",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar Global Controls ---
st.sidebar.title("Energy Transition Intel")
st.sidebar.markdown("---")

cohort_countries = [
    "Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda", 
    "Ghana", "Nigeria", "South Africa", "Egypt", "Morocco"
]

# Global Country Selector 
selected_country = st.sidebar.selectbox(
    "Global Country Focus", 
    cohort_countries,
    key="selected_country"
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Navigation Guide:\n"
    "Use the page menu above to switch between views."
)

# --- Main Overview Content ---
st.title("African Electricity Transition Intelligence Dashboard")
st.markdown(
    "#### Evidence-Based Energy Transition Analytics Across 10 Strategic African Nations"
)
st.markdown(
    "This platform tracks power generation mixes, renewable energy integration, "
    "grid access electrification, and decarbonization pathways across key economic hubs in Africa."
)

st.markdown("---")

# Fetch summary for selected country
summary = get_country_summary(selected_country)

st.subheader(f"Strategic Snapshot: {selected_country}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label=f"Total Generation ({summary['latest_year']})", 
        value=f"{summary['total_generation_twh']:,.2f} TWh"
    )

with col2:
    st.metric(
        label="Clean Energy Share", 
        value=f"{summary['clean_share_pct']:.1f}%"
    )

with col3:
    st.metric(
        label=f"Electricity Access ({summary['access_rate_year']})", 
        value=f"{summary['access_rate_pct']:.1f}% of Pop."
    )

with col4:
    st.metric(
        label="Target Cohort Rank", 
        value="Tier-1 Hub"
    )

st.markdown("---")

# Cohort Comparison Preview Table
st.subheader("Cohort Quick Comparison")

cohort_data = []
for c in cohort_countries:
    s = get_country_summary(c)
    cohort_data.append({
        "Country": s["country"],
        "Latest Year": s["latest_year"],
        "Total Generation (TWh)": s["total_generation_twh"],
        "Clean Share (%)": s["clean_share_pct"],
        "Access Rate (%)": s["access_rate_pct"]
    })

df_cohort = pd.DataFrame(cohort_data).sort_values(by="Total Generation (TWh)", ascending=False)
st.dataframe(df_cohort, use_container_width=True, hide_index=True)