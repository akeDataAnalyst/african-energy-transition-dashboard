import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.metrics import get_latest_generation_mix, get_country_summary
import plotly.express as px

# Sidebar Global Controls
st.sidebar.title("Energy Transition Intel")
st.sidebar.markdown("---")
cohort_countries = ["Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda", "Ghana", "Nigeria", "South Africa", "Egypt", "Morocco"]
selected_country = st.sidebar.selectbox("Global Country Focus", cohort_countries, key="selected_country")
st.sidebar.markdown("---")

st.title("Electricity Mix & Technology Breakdown")
st.markdown(f"Analyzing disaggregated generation sources for **{selected_country}**.")

summary = get_country_summary(selected_country)
df_mix = get_latest_generation_mix(selected_country)

if not df_mix.empty:
    fig = px.bar(
        df_mix,
        x="source",
        y="generation_twh",
        text="generation_twh",
        labels={"source": "Electricity Source", "generation_twh": "Generation (TWh)"},
        title=f"Generation by Technology in {summary['latest_year']}",
        color="source",
        template="plotly_white"
    )
    fig.update_traces(texttemplate='%{text:.2f} TWh', textposition='outside')
    fig.update_layout(xaxis_tickangle=-45, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available.")