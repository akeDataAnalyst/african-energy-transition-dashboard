"""
Backend helper functions to query DuckDB and compute core indicators
for the African Electricity Transition Intelligence Dashboard.
"""

from pathlib import Path
import duckdb
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "energy_transition.db"

def get_connection():
    """Returns a connection to the DuckDB database."""
    return duckdb.connect(str(DB_PATH), read_only=True)

def get_latest_generation_mix(country: str) -> pd.DataFrame:
    """
    Retrieves the disaggregated generation mix for a specific country 
    for the most recent available year, excluding aggregate rows.
    """
    conn = get_connection()
    query = """
        SELECT 
            "Electricity source" AS source,
            "Generation (TWh)" AS generation_twh,
            "Share of generation (%)" AS share_pct,
            Year AS year
        FROM ember_data
        WHERE Clean_Country = ? 
          AND "Is aggregated source" = 0
          AND Year = (SELECT MAX(Year) FROM ember_data WHERE Clean_Country = ?)
        ORDER BY "Generation (TWh)" DESC;
    """
    df = conn.execute(query, [country, country]).df()
    conn.close()
    return df

def get_country_summary(country: str) -> dict:
    """
    Computes high-level summary stats for a country (Total Generation, Demand, 
    Latest Clean Share, and Latest Electricity Access Rate).
    """
    conn = get_connection()
    
    # Get latest total generation and demand from Ember aggregates
    gen_query = """
        SELECT Year, "Generation (TWh)" 
        FROM ember_data 
        WHERE Clean_Country = ? AND "Electricity source" = 'Total generation'
        ORDER BY Year DESC LIMIT 1;
    """
    gen_res = conn.execute(gen_query, [country]).fetchone()
    
    # Get latest clean/renewable share
    clean_query = """
        SELECT "Share of generation (%)" 
        FROM ember_data 
        WHERE Clean_Country = ? AND "Electricity source" = 'Clean'
        ORDER BY Year DESC LIMIT 1;
    """
    clean_res = conn.execute(clean_query, [country]).fetchone()
    
    # Get latest World Bank electricity access rate
    access_query = """
        SELECT Value, Year 
        FROM world_bank_data 
        WHERE Clean_Country = ? AND "Indicator Code" = 'EG.ELC.ACCS.ZS'
        ORDER BY Year DESC LIMIT 1;
    """
    access_res = conn.execute(access_query, [country]).fetchone()
    
    conn.close()
    
    return {
        "country": country,
        "latest_year": gen_res[0] if gen_res else None,
        "total_generation_twh": gen_res[1] if gen_res else 0.0,
        "clean_share_pct": clean_res[0] if clean_res else 0.0,
        "access_rate_pct": access_res[0] if access_res else 0.0,
        "access_rate_year": access_res[1] if access_res else None
    }