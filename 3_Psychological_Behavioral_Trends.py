import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

# ✅ FIXED: Use valid Seaborn palette
sns.set_theme(style="whitegrid", palette="flare")  # 'flare' gives warm pink tones

st.title("🧠 Objective 3: Psychological & Behavioral Trends")
st.info("To explore how psychological factors, especially insomnia (AIS), correlate with addiction (BFAS Total).")

st.divider()

# Visualization 7: Line (AIS vs Average BFAS)
avg_bfas = df.groupby("AIS 0-1")["BFAS total"].mean().reset_index()
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(x="AIS 0-1", y="BFAS total", data=avg_bfas, marker="o", color="#ff5c8d")
ax.set_title("Average BFAS Total by AIS (Insomnia Score)", color="#d63384")
st.pyplot(fig)

st.divider()

# Visualization 8: Correlation Heatmap
corr = df[["Age", "BFAS total", "Sex01", "AIS 0-1"]].corr()
fig, ax = plt.subplots(figsize=(7,5))
sns.heatmap(corr, annot=True, cmap="RdPu", ax=ax)
ax.set_title("Correlation Matrix among Key Variables", color="#d63384")
st.pyplot(fig)

st.divider()

# Visualization 9: 3D Scatter (Age, BFAS, AIS)
fig = px.scatter_3d(
    df,
    x="Age",
    y="BFAS total",
    z="AIS 0-1",
    color="Sex",
    color_discrete_map={"Male": "#69b3a2", "Female": "#ff5c8d"},
    title="3D Relationship: Age, BFAS Total, and AIS"
)
st.plotly_chart(fig, use_container_width=True)

st.success("Insight: Higher insomnia scores (AIS) are strongly linked with higher BFAS totals, indicating that sleep disturbance may contribute to increased addiction severity and depressive symptoms among students.")
