import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

# Aesthetic setup
sns.set_theme(style="whitegrid", palette="viridis")

st.title("🎯 Objective 1: Demographic Distribution")
st.info("To analyze the demographic distribution of respondents based on age, gender, and employment type.")

st.markdown("---")

# Visualization 1: Age distribution (Histogram)
fig, ax = plt.subplots(figsize=(7,4))
sns.histplot(df["Age"], bins=10, kde=True, color="#8E44AD", ax=ax)
ax.set_title("Age Distribution of Respondents", fontsize=13, fontweight="bold")
st.pyplot(fig)

st.markdown("---")

# Visualization 2: Gender ratio (Pie Chart)
fig, ax = plt.subplots(figsize=(5,5))
gender_counts = df["Sex"].value_counts()
colors = ["#3498DB", "#E74C3C", "#9B59B6"]
ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90, colors=colors)
ax.set_title("Gender Ratio of Respondents", fontsize=13, fontweight="bold")
st.pyplot(fig)

st.markdown("---")

# Visualization 3: Employment vs Economic Status (Grouped Bar)
fig, ax = plt.subplots(figsize=(9,5))
sns.countplot(data=df, x="Employment", hue="Economic status", palette="coolwarm", ax=ax)
ax.set_title("Employment Type by Economic Status", fontsize=13, fontweight="bold")
ax.set_xlabel("Employment Type")
ax.set_ylabel("Number of Respondents")
ax.legend(title="Economic Status")
plt.xticks(rotation=20)
st.pyplot(fig)

st.success("Insight: Respondents are mostly young adults with diverse employment and economic backgrounds, showing a balanced gender mix.")
