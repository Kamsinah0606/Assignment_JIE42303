import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("1️⃣ Demographic Distribution")

# Load dataset
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/main/DataBase.xlsx"
df = pd.read_excel(DATA_URL)

st.subheader("Objective:")
st.info("To analyze the demographic distribution of respondents based on age, gender, and employment type.")

# Visualization 1: Age distribution
fig, ax = plt.subplots(figsize=(6,4))
sns.histplot(df["Age"], bins=10, kde=True, ax=ax)
ax.set_title("Age Distribution of Respondents")
st.pyplot(fig)

# Visualization 2: Gender ratio
fig, ax = plt.subplots(figsize=(5,5))
gender_counts = df["Sex"].value_counts()
ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
ax.set_title("Gender Ratio")
st.pyplot(fig)

# Visualization 3: Employment distribution
fig, ax = plt.subplots(figsize=(8,4))
sns.countplot(y="Employment", data=df, order=df["Employment"].value_counts().index, ax=ax)
ax.set_title("Employment Distribution")
st.pyplot(fig)

st.success("Insight: The dataset is dominated by young adults with varied employment statuses, showing balanced gender representation.")
