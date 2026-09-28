import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.metrics import get_connection
import plotly.express as px

# Sidebar Global Controls
st.sidebar.title("Energy Transition Intel")
st.sidebar.markdown("---")
cohort_countries = ["Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda", "Ghana", "Nigeria", "South Africa", "Egypt", "Morocco"]
selected_country = st.sidebar.selectbox("Global Country Focus", cohort_countries, key="selected_country")
st.sidebar.markdown("---")

st.title("Regional Cohort Comparison")
st.markdown("Comparing clean energy shares across all 10 African target nations.")

conn = get_connection()
query = """
    SELECT Clean_Country AS Country, Year, "Share of generation (%)" AS Clean_Share
    FROM ember_data
    WHERE "Electricity source" = 'Clean' 
      AND Year = (SELECT MAX(Year) FROM ember_data)
    ORDER BY Clean_Share DESC;
"""
df_comp = conn.execute(query).df()
conn.close()

if not df_comp.empty:
    fig = px.bar(
        df_comp,
        x="Country",
        y="Clean_Share",
        text="Clean_Share",
        title="Clean Energy Share (%) Across Cohort (Latest Year)",
        labels={"Clean_Share": "Clean Generation Share (%)", "Country": "Country"},
        color="Clean_Share",
        color_continuous_scale="Viridis",
        template="plotly_white"
    )
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(xaxis_tickangle=-45, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No comparison data available.")