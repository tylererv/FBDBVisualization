# main.py
import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# Import our custom modules
import database as db
import visuals as viz

# -----------------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="NFLDB Analytics",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("Settings")
    season = st.selectbox("Select Season", ["2024", "2023", "2022"])
    st.write("Data Source: Local MS Access DB")

# -----------------------------------------------------------------------------
# MAIN LAYOUT
# -----------------------------------------------------------------------------

# 1. Header Section with Animation
col1, col2 = st.columns([1, 4])

with col1:
    # This is a free Lottie animation of a football player
    lottie_football = load_lottieurl("https://lottie.host/9ea6adc7-341f-44c3-b5c2-9ac701873d57/TWoBUq01BK.json")
    st_lottie(lottie_football, height=150, key="football_anim")

with col2:
    st.title("Pro Football Database Dashboard")
    st.markdown(f"### Season Analysis: {season}")

st.markdown("---") # Horizontal line separator

# 2. Data Loading
# We query the DB here. If your table names are different, change the SQL below!
sql_query = "SELECT * FROM Players;" 
df = db.get_data(sql_query)

# 3. Top Level KPIs (Key Performance Indicators)
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Top Passer", value="P. Mahomes", delta="305 yds")
kpi2.metric(label="Touchdown Leader", value="J. Allen", delta="4 TDs")
kpi3.metric(label="Total Games", value=str(len(df)), delta="Week 2")

st.markdown("### Player Momentum")

# 4. The Animated Chart
# We call the function from visuals.py
chart_fig = viz.plot_qb_performance(df)
st.plotly_chart(chart_fig, use_container_width=True)

# 5. Raw Data View (Expandable)
with st.expander("View Raw Database Records"):
    st.dataframe(df, use_container_width=True)