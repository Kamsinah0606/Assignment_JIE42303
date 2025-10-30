import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="The indirect effect of TikTok use on depressive symptoms through insomnia among university students",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"

try:
    df = pd.read_csv(DATA_URL, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(DATA_URL, encoding="ISO-8859-1", errors="replace")

# -----------------------------
# Header
# -----------------------------
st.title("📊 Scientific Visualization – JIE42303")

# -------------------------------
# Define all pages
# -------------------------------

home = st.Page(
    "homepage.py", 
    title="Homepage", 
    icon=":material/home:", 
    default=True)

objective_1 = st.Page(
    "1_Demographic_Distribution.py",
    title="Objective 1",
    icon=":material/analytics:",
    default=True
)

objective_2 = st.Page(
    "2_Social_Factors_vs_Addiction.py",
    title="Objective 2",
    icon=":material/groups:"
)

objective_3 = st.Page(
    "3_Psychological_Behavioral_Trends.py",
    title="Objective 3",
    icon=":material/psychology:"
)

# -----------------------------
# Navigation Menu
# -----------------------------
pg = st.navigation({
    "Menu": [home, objective_1, objective_2, objective_3]
                   })

pg.run()


# ------------------------------------------------
# Homepage Content
# ------------------------------------------------
st.title("🎓 Student Survey Data Visualization")
st.markdown("""
Welcome to the **Student Survey Dashboard**.

This Streamlit app visualizes and analyzes data from the student survey dataset.  
Use the navigation menu above to explore each objective:

1️⃣ **Demographic Distribution**  
2️⃣ **Social Factors vs Addiction**  
3️⃣ **Psychological & Behavioral Trends**
""")
