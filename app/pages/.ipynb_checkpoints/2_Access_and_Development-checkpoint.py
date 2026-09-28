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

st.title("Access & Socio-Economic Development")
st.markdown(f"Historical electricity access rates (% of population) for **{selected_country}** (World Bank WDI).")

conn = get_connection()
query = """
    SELECT Year, Value AS Access_Rate_Pct
    FROM world_bank_data
    WHERE Clean_Country = ? AND "Indicator Code" = 'EG.ELC.ACCS.ZS'
    ORDER BY Year ASC;
"""
df_access = conn.execute(query, [selected_country]).df()
conn.close()

if not df_access.empty:
    fig = px.line(
        df_access,
        x="Year",
        y="Access_Rate_Pct",
        markers=True,
        title=f"Electricity Access Rate Over Time — {selected_country}",
        labels={"Access_Rate_Pct": "Access Rate (% of Population)", "Year": "Year"},
        template="plotly_white"
    )
    fig.update_layout(yaxis=dict(range=[0, 105]))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No World Bank access data found for this country.")