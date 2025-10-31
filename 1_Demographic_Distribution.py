import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="rocket")

st.title("🌸 Objective 1: Demographic Distribution")
st.info("To analyze the demographic distribution of respondents based on age, gender, and employment type.")

DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase_Preprocessed.csv"
df = pd.read_csv(DATA_URL)

plt.rcParams['axes.facecolor'] = '#fff8f9'
plt.rcParams['figure.facecolor'] = '#fff8f9'

st.divider()

# V1: Histogram — Age Distribution
fig, ax = plt.subplots(figsize=(6,4))
sns.histplot(df["Age"], bins=10, kde=True, ax=ax, color="#ff80ab")
ax.set_title("Age Distribution of Respondents", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📊 Summary:</h5>
<p style='color:#4a235a;'>Most respondents are between 20–25 years old, showing that the sample largely represents young adults — the main demographic of university students.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# V2: Pie Chart — Gender Ratio
fig, ax = plt.subplots(figsize=(5,5))
gender_counts = df["Sex"].value_counts()
ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%",
       startangle=90, colors=["#ffb6c1","#b39ddb","#f3e5f5"])
ax.set_title("Gender Distribution", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>💬 Summary:</h5>
<p style='color:#4a235a;'>The gender ratio is fairly balanced, ensuring that comparisons across behavioral and psychological aspects are representative.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# V3: Grouped Bar — Employment × Economic Status
fig, ax = plt.subplots(figsize=(8,5))
grouped = df.groupby(["Employment","Economic status"])["BFAS total"].count().reset_index()
sns.barplot(x="Economic status", y="BFAS total", hue="Employment", data=grouped, ax=ax)
ax.set_title("Employment vs Economic Status Distribution", color="#4a235a")
ax.legend(title="Employment", bbox_to_anchor=(1,1))
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📈 Summary:</h5>
<p style='color:#4a235a;'>Most respondents report moderate economic status, with students dominating across categories — typical of a university population.</p>
</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("""
<div style='background-color:#f3e5f5;padding:20px;border-radius:15px;'>
<h4 style='color:#4a235a;'>🌼 Overall Objective 1 Summary</h4>
<p style='color:#4a235a;'>The dataset reflects a young, balanced demographic primarily composed of students with varied financial backgrounds, forming a strong base for behavioral analysis.</p>
</div>
""", unsafe_allow_html=True)
