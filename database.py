# "C:\Users\tyerv\Documents\Programs\VSC\NFLDBpy.accdb"

# database.py
import pyodbc
import pandas as pd
import streamlit as st

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# UPDATE THIS PATH to point to your actual .accdb file
DB_PATH = r"C:\Users\tyerv\Documents\Programs\VSC\NFLDBpy.accdb"

# -----------------------------------------------------------------------------
# DATABASE FUNCTIONS
# -----------------------------------------------------------------------------

@st.cache_data
def get_data(query):
    """
    Connects to MS Access and returns a dataframe based on the query.
    Includes error handling to fallback to mock data if DB isn't found.
    """
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={DB_PATH};"
    )
    
    try:
        conn = pyodbc.connect(conn_str)
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"⚠️ Database Error: {e}")
        st.warning("⚠️ Loading MOCK DATA instead so you can see the UI.")
        return get_mock_data()

def get_mock_data():
    """
    Generates fake NFL data for testing purposes.
    """
    data = {
        "Player": ["Patrick Mahomes", "Josh Allen", "Lamar Jackson", "Joe Burrow", 
                   "Patrick Mahomes", "Josh Allen", "Lamar Jackson", "Joe Burrow"],
        "Week": [1, 1, 1, 1, 2, 2, 2, 2],
        "PassingYards": [290, 310, 250, 200, 305, 280, 270, 240],
        "Touchdowns": [3, 2, 2, 1, 4, 3, 2, 2],
        "Team": ["KC", "BUF", "BAL", "CIN", "KC", "BUF", "BAL", "CIN"]
    }
    return pd.DataFrame(data)