import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

sns.set_theme(style="whitegrid", palette="mako")

st.title("💜 Objective 2: Social Factors vs Addiction (BFAS Total)")
st.info("To examine how social factors such as gender, age, and employment relate to addiction levels (BFAS Total).")

DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)
df["Sex"] = df["Sex"].str.strip().str.title()

# Match figure background
plt.rcParams['axes.facecolor'] = '#fff8f9'
plt.rcParams['figure.facecolor'] = '#fff8f9'

st.divider()

# Visualization 4: Boxplot
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(
    x="Sex", y="BFAS total", data=df, ax=ax,
    palette={"Male": "#6a5acd", "Female": "#ff80ab", "I Do Not Want To Disclose": "#b39ddb"}
)
ax.set_title("BFAS Total by Gender", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📊 Summary:</h5>
  <p style='color:#4a235a;'>Female participants tend to show slightly higher BFAS totals, suggesting higher engagement or vulnerability to social media influence.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Visualization 5: Scatter Plot
fig = px.scatter(
    df, x="Age", y="BFAS total", color="Sex",
    title="Age vs BFAS Total",
    color_discrete_map={"Female": "#ff80ab", "Male": "#6a5acd", "I Do Not Want To Disclose": "#b39ddb"}
)
fig.update_layout(paper_bgcolor="#fff8f9", plot_bgcolor="#fff8f9")
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📈 Summary:</h5>
  <p style='color:#4a235a;'>BFAS scores decrease slightly with age, showing that younger respondents are more likely to develop higher addiction tendencies.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Visualization 6: Heatmap
pivot = df.pivot_table(index="Employment", columns="Economic status", values="BFAS total", aggfunc="mean")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(pivot, annot=True, cmap="RdPu", ax=ax)
ax.set_title("Mean BFAS by Employment and Economic Status", color="#4a235a")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>🔥 Summary:</h5>
  <p style='color:#4a235a;'>Respondents with lower economic stability and flexible jobs tend to show higher addiction, indicating that stress factors might play a role.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px;'>
  <h4 style='color:#4a235a;'>💬 Overall Objective 2 Summary</h4>
  <p style='color:#4a235a;'>Social environment influences addiction behavior. Age, gender, employment, and economy interact to affect online dependency intensity.</p>
</div>
""", unsafe_allow_html=True)
