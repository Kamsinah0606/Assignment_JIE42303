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

# Match figure background
plt.rcParams['axes.facecolor'] = '#fff8f9'
plt.rcParams['figure.facecolor'] = '#fff8f9'

st.divider()

# Visualization 7: Line Plot
avg_bfas = df.groupby("AIS 0-1")["BFAS total"].mean().reset_index()
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(x="AIS 0-1", y="BFAS total", data=avg_bfas, marker="o", color="#d63384")
ax.set_title("Average BFAS Total by AIS (Insomnia Score)", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📊 Summary:</h5>
  <p style='color:#4a235a;'>Higher insomnia levels (AIS) are correlated with higher BFAS totals, suggesting that sleep issues may elevate social media dependence.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Visualization 8: Correlation Heatmap
corr = df[["Age", "BFAS total", "Sex01", "AIS 0-1"]].corr()
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="RdPu", ax=ax)
ax.set_title("Correlation Matrix among Key Variables", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>💬 Summary:</h5>
  <p style='color:#4a235a;'>Insomnia and addiction (AIS & BFAS) are moderately correlated, while age has a weaker relationship, highlighting a behavioral health pattern.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Visualization 9: 3D Scatter
fig = px.scatter_3d(
    df, x="Age", y="BFAS total", z="AIS 0-1", color="Sex",
    color_discrete_map={"Male": "#69b3a2", "Female": "#ff5c8d", "I Do Not Want To Disclose": "#b39ddb"},
    title="3D Relationship: Age, BFAS Total, and AIS"
)
fig.update_layout(paper_bgcolor="#fff8f9", plot_bgcolor="#fff8f9")
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>🧠 Summary:</h5>
  <p style='color:#4a235a;'>Younger participants with higher AIS and BFAS values form a dense cluster, reinforcing the connection between poor sleep and higher addiction.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px;'>
  <h4 style='color:#4a235a;'>💖 Overall Objective 3 Summary</h4>
  <p style='color:#4a235a;'>Insomnia and social media dependency interact meaningfully, suggesting that sleep deprivation amplifies behavioral addiction among students.</p>
</div>
""", unsafe_allow_html=True)
