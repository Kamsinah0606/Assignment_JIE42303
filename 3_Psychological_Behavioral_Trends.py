import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

sns.set_theme(style="whitegrid", palette="flare")

st.title("💖 Objective 3: Psychological & Behavioral Trends")
st.info("To explore correlations between psychological factors (AIS) and addiction scores (BFAS Total).")

# Load dataset
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

st.divider()

# ------------------------------------------------
# Visualization 7: Line Plot (AIS vs BFAS)
# ------------------------------------------------
avg_bfas = df.groupby("AIS 0-1")["BFAS total"].mean().reset_index()
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(x="AIS 0-1", y="BFAS total", data=avg_bfas, marker="o", color="#d63384")
ax.set_title("Average BFAS Total by AIS (Insomnia Score)")
st.pyplot(fig)

# Summary 1
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📊 Summary:</h5>
  <p style='color:#4a235a;'>
  There is a noticeable positive trend — as insomnia scores (AIS) increase, 
  the average BFAS total also rises, indicating that sleep problems are linked 
  with higher social media dependency.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Visualization 8: Correlation Heatmap
# ------------------------------------------------
corr = df[["Age", "BFAS total", "Sex01", "AIS 0-1"]].corr()
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="RdPu", ax=ax)
ax.set_title("Correlation Matrix among Key Variables")
st.pyplot(fig)

# Summary 2
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>💬 Summary:</h5>
  <p style='color:#4a235a;'>
  The correlation map confirms moderate positive associations between insomnia (AIS) and BFAS total, 
  while age shows a weak negative correlation, suggesting younger students experience 
  higher addiction intensity.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Visualization 9: 3D Scatter Plot (Age, BFAS, AIS)
# ------------------------------------------------
fig = px.scatter_3d(
    df,
    x="Age",
    y="BFAS total",
    z="AIS 0-1",
    color="Sex",
    color_discrete_map={
        "Male": "#69b3a2",
        "Female": "#ff5c8d",
        "I Do Not Want To Disclose": "#b39ddb"
    },
    title="3D Relationship: Age, BFAS Total, and AIS"
)
st.plotly_chart(fig, use_container_width=True)

# Summary 3
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>🧠 Summary:</h5>
  <p style='color:#4a235a;'>
  The 3D scatter illustrates that higher AIS and BFAS values cluster among younger respondents, 
  reinforcing the trend that poor sleep and digital habits intertwine strongly in younger age groups.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Final Objective Summary
# ------------------------------------------------
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px;'>
  <h4 style='color:#4a235a;'>💖 Overall Objective 3 Summary</h4>
  <p style='color:#4a235a;'>
  Psychological behavior patterns indicate a clear connection between insomnia (AIS) and social media addiction (BFAS). 
  The findings imply that emotional strain and disrupted sleep can significantly contribute to problematic online behavior.
  </p>
</div>
""", unsafe_allow_html=True)
