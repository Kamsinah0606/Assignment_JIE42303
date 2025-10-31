import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set Seaborn theme
sns.set_theme(style="whitegrid", palette="mako")

# Page title
st.title("💜 Objective 2: Social Factors vs Addiction (BFAS Total)")
st.info("To examine how social factors such as gender, age, and employment relate to addiction levels (BFAS Total).")

# Load dataset
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

# Clean up "Sex" values (to prevent ValueError)
df["Sex"] = df["Sex"].str.strip().str.title()  # Example: 'male' → 'Male'

st.divider()

# ------------------------------------------------
# Visualization 4: Boxplot by Gender
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(
    x="Sex",
    y="BFAS total",
    data=df,
    ax=ax,
    palette={
        "Male": "#6a5acd",
        "Female": "#ff80ab",
        "I Do Not Want To Disclose": "#b39ddb"
    }
)
ax.set_title("BFAS Total by Gender")
st.pyplot(fig)

# Summary for Visualization 4
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📊 Summary:</h5>
  <p style='color:#4a235a;'>
  The boxplot reveals that female respondents tend to have slightly higher BFAS total scores compared to males, 
  indicating potentially greater social media engagement among female students. 
  The third category remains limited but shows moderate variability.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Visualization 5: Scatter Plot (Age vs BFAS Total)
# ------------------------------------------------
fig = px.scatter(
    df,
    x="Age",
    y="BFAS total",
    color="Sex",
    title="Age vs BFAS Total",
    color_discrete_map={
        "Female": "#ff80ab",
        "Male": "#6a5acd",
        "I Do Not Want To Disclose": "#b39ddb"
    }
)
st.plotly_chart(fig, use_container_width=True)

# Summary for Visualization 5
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>📈 Summary:</h5>
  <p style='color:#4a235a;'>
  The scatter plot shows a mild negative trend, where BFAS scores tend to decrease as age increases. 
  Younger respondents report higher addiction levels, which may be due to greater online engagement frequency.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Visualization 6: Heatmap (Employment vs Economic Status)
# ------------------------------------------------
pivot = df.pivot_table(index="Employment", columns="Economic status", values="BFAS total", aggfunc="mean")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(pivot, annot=True, cmap="RdPu", ax=ax)
ax.set_title("Mean BFAS by Employment and Economic Status")
st.pyplot(fig)

# Summary for Visualization 6
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px;'>
  <h5 style='color:#4a235a;'>🔥 Summary:</h5>
  <p style='color:#4a235a;'>
  The heatmap indicates that individuals with unstable or part-time employment and lower economic status 
  tend to have higher mean BFAS scores, suggesting social and financial stressors could heighten online dependency.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# Final Objective Summary
# ------------------------------------------------
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px;'>
  <h4 style='color:#4a235a;'>💬 Overall Objective 2 Summary</h4>
  <p style='color:#4a235a;'>
  Social variables such as age, gender, employment, and economic status significantly affect social media addiction levels. 
  Younger participants and those with more uncertain job or financial conditions tend to report higher addiction intensity.
  </p>
</div>
""", unsafe_allow_html=True)
