import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

# Theme
sns.set_theme(style="whitegrid", palette="flare")

st.title("🎯 Objective 1: Demographic Distribution")
st.info("To analyze the demographic distribution of respondents based on age, gender, and employment type.")

st.divider()

# Visualization 1: Age Distribution
fig, ax = plt.subplots(figsize=(7,4))
sns.histplot(df["Age"], bins=10, kde=True, ax=ax, color="#ff5c8d")
ax.set_title("Age Distribution of Respondents", fontsize=12, color="#d63384")
st.pyplot(fig)

st.divider()

# Visualization 2: Gender Ratio (Pie Chart)
fig, ax = plt.subplots(figsize=(5,5))
gender_counts = df["Sex"].value_counts()
ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90,
       colors=["#ff7eb9", "#ff65a3", "#7afcff"])
ax.set_title("Gender Ratio of Respondents", color="#d63384")
st.pyplot(fig)

st.divider()

# Visualization 3: Employment by Economic Status (Grouped Bar)
fig, ax = plt.subplots(figsize=(8,5))
sns.countplot(data=df, x="Employment", hue="Economic status", ax=ax, palette="flare")
ax.set_title("Employment Type by Economic Status", color="#d63384")
ax.set_xlabel("Employment Type")
ax.set_ylabel("Number of Respondents")
ax.legend(title="Economic Status")
st.pyplot(fig)

st.success("Insight: Respondents are mostly young adults (ages 21–25) with a balanced gender mix and diverse employment and economic backgrounds, reflecting a representative sample of university students.")
