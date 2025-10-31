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

# Match figure background to Streamlit theme
plt.rcParams['axes.facecolor'] = '#fff8f9'
plt.rcParams['figure.facecolor'] = '#fff8f9'

st.divider()

# ------------------------------------------------
# Visualization 1: Age Distribution
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(6,4))
sns.histplot(df["Age"], bins=10, kde=True, ax=ax, color="#ff80ab")
ax.set_title("Age Distribution of Respondents", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📊 Summary:</h5>
  <p style='color:#4a235a;'>Most respondents are young adults, indicating that the data reflects university-age participants with minimal age variation.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Visualization 2: Gender Ratio
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(5,5))
gender_counts = df["Sex"].value_counts()
ax.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#ffb6c1", "#b39ddb", "#f3e5f5"]
)
ax.set_title("Gender Ratio", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>💬 Summary:</h5>
  <p style='color:#4a235a;'>Gender distribution is relatively balanced, allowing fair comparisons between male and female respondents.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Visualization 3: Employment Distribution
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(8,4))
sns.countplot(y="Employment", data=df, order=df["Employment"].value_counts().index, ax=ax, color="#ce93d8")
ax.set_title("Employment Distribution", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📈 Summary:</h5>
  <p style='color:#4a235a;'>Most respondents are either students or part-time workers, highlighting typical student lifestyles.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Final Summary
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px;'>
  <h4 style='color:#4a235a;'>🌼 Overall Objective 1 Summary</h4>
  <p style='color:#4a235a;'>This demographic overview sets a foundation for behavioral and psychological analysis, showing young, balanced, and diverse participants.</p>
</div>
""", unsafe_allow_html=True)
