import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

sns.set_theme(style="whitegrid", palette="flare")

st.title("💖 Objective 3: Psychological & Behavioral Trends")
st.info("To explore correlations between psychological factors (AIS) and addiction scores (BFAS Total).")

DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

st.divider()

# Visualization 7: Line plot (AIS vs BFAS)
avg_bfas = df.groupby("AIS 0-1")["BFAS total"].mean().reset_index()
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(x="AIS 0-1", y="BFAS total", data=avg_bfas, marker="o", color="#d63384")
ax.set_title("Average BFAS Total by AIS (Insomnia Score)")
st.pyplot(fig)

# Visualization 8: Correlation heatmap
st.divider()
corr = df[["Age", "BFAS total", "Sex01", "AIS 0-1"]].corr()
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="RdPu", ax=ax)
ax.set_title("Correlation Matrix among Key Variables")
st.pyplot(fig)

# Visualization 9: 3D Scatter
st.divider()
fig = px.scatter_3d(
    df,
    x="Age",
    y="BFAS total",
    z="AIS 0-1",
    color="Sex",
    color_discrete_map={"Male": "#69b3a2", "Female": "#ff5c8d", "I do not want to disclose": "#b39ddb"},
    title="3D Relationship: Age, BFAS Total, and AIS"
)
st.plotly_chart(fig, use_container_width=True)

# Summary Box
st.markdown("""
<div style='background-color:#f5e6fa; padding:20px; border-radius:15px;'>
  <h4 style='color:#4a235a;'>🧠 Summary Insight</h4>
  <p style='color:#4a235a;'>
  Higher AIS (insomnia) scores correlate with higher BFAS totals, indicating that sleep problems may intensify 
  social media dependency and depressive symptoms among university students.
  </p>
</div>
""", unsafe_allow_html=True)
