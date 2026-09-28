"""
Ingests cleaned CSV datasets (Ember electricity data & World Bank indicators)
into a local DuckDB analytical database for fast, memory-efficient querying.
"""

import duckdb
import os

def run_ingestion():
    # Define database path
    db_path = "data/energy_transition.db"
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to DuckDB
    conn = duckdb.connect(db_path)
    print(f"Connected to DuckDB database at: {db_path}")
    
    # 1. Ingest Cleaned Ember Data
    ember_csv = "data/processed/ember_cleaned.csv"
    if os.path.exists(ember_csv):
        conn.execute(f"""
            CREATE OR REPLACE TABLE ember_data AS 
            SELECT * FROM read_csv_auto('{ember_csv}');
        """)
        row_count = conn.execute("SELECT COUNT(*) FROM ember_data").fetchone()[0]
        print(f"Successfully loaded 'ember_data' table into DuckDB ({row_count:,} rows).")
    else:
        print(f"Warning: {ember_csv} not found. Please ensure cleaning notebook was run.")

    # 2. Ingest Cleaned World Bank Data
    wb_csv = "data/processed/world_bank_cleaned.csv"
    if os.path.exists(wb_csv):
        conn.execute(f"""
            CREATE OR REPLACE TABLE world_bank_data AS 
            SELECT * FROM read_csv_auto('{wb_csv}');
        """)
        row_count = conn.execute("SELECT COUNT(*) FROM world_bank_data").fetchone()[0]
        print(f"Successfully loaded 'world_bank_data' table into DuckDB ({row_count:,} rows).")
    else:
        print(f"Warning: {wb_csv} not found. Please ensure cleaning notebook was run.")

    # Close connection
    conn.close()
    print("Ingestion pipeline complete! DuckDB database is ready for analytics.")

if __name__ == "__main__":
    run_ingestion()