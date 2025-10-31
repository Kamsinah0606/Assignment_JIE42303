import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

sns.set_theme(style="whitegrid", palette="mako")

st.title("💜 Objective 2: Social Factors vs Addiction (BFAS Total)")
st.info("To examine how social factors such as gender, age, and economic status relate to addiction levels (BFAS Total).")

DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)
df["Sex"] = df["Sex"].str.strip().str.title()

plt.rcParams['axes.facecolor'] = '#fff8f9'
plt.rcParams['figure.facecolor'] = '#fff8f9'

st.divider()

# V4: Boxplot — BFAS Total by Gender
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(x="Sex", y="BFAS total", data=df, ax=ax,
    palette={"Male":"#6a5acd","Female":"#ff80ab","I Do Not Want To Disclose":"#b39ddb"})
ax.set_title("BFAS Total by Gender", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📊 Summary:</h5>
<p style='color:#4a235a;'>Female respondents show slightly higher BFAS totals, possibly indicating greater social engagement or emotional connectivity through online platforms.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# V5: Scatter Plot — Age vs BFAS (color by Sex)
fig = px.scatter(
    df, x="Age", y="BFAS total", color="Sex",
    color_discrete_map={"Female":"#ff80ab","Male":"#6a5acd","I Do Not Want To Disclose":"#b39ddb"},
    title="Age vs BFAS Total"
)
fig.update_layout(paper_bgcolor="#fff8f9", plot_bgcolor="#fff8f9")
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📈 Summary:</h5>
<p style='color:#4a235a;'>A downward trend suggests that younger individuals report higher BFAS totals, highlighting age as a potential risk factor for online addiction.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# V6: Violin Plot — Economic Status vs BFAS Total
fig, ax = plt.subplots(figsize=(8,5))
sns.violinplot(x="Economic status", y="BFAS total", data=df, ax=ax, palette="RdPu")
ax.set_title("Distribution of BFAS Total by Economic Status", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>🎻 Summary:</h5>
<p style='color:#4a235a;'>Respondents with lower economic stability exhibit higher variability in BFAS scores, suggesting stress or coping behavior linked to online use.</p>
</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("""
<div style='background-color:#f3e5f5;padding:20px;border-radius:15px;'>
<h4 style='color:#4a235a;'>💬 Overall Objective 2 Summary</h4>
<p style='color:#4a235a;'>Social context strongly shapes addiction behavior — gender, age, and financial conditions interact to influence social media dependence intensity.</p>
</div>
""", unsafe_allow_html=True)
