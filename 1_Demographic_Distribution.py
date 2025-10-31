import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="rocket")

st.title("🌸 Objective 1: Demographic Distribution")
st.info("To analyze the demographic distribution of respondents based on age, gender, and employment type.")

# Load dataset
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

st.divider()

# ------------------------------------------------
# Visualization 1: Age Distribution
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(6,4))
sns.histplot(df["Age"], bins=10, kde=True, ax=ax, color="#ff80ab")
ax.set_title("Age Distribution of Respondents")
st.pyplot(fig)

# Summary 1
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📊 Summary:</h5>
  <p style='color:#4a235a;'>
  Most respondents are concentrated within the young adult age range, 
  suggesting a primary population of university students or early-career individuals.
  The smooth distribution curve shows few outliers in older age categories.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Visualization 2: Gender Ratio
# ------------------------------------------------
