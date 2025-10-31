import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# ------------------------------------------------
# Theme & Plot Settings
# ------------------------------------------------
theme_bg = "#fff8f9"
theme_text = "#4a235a"
theme_primary = "#d63384"

plt.rcParams['figure.facecolor'] = theme_bg
plt.rcParams['axes.facecolor'] = theme_bg
plt.rcParams['text.color'] = theme_text
plt.rcParams['axes.labelcolor'] = theme_text
plt.rcParams['xtick.color'] = theme_text
plt.rcParams['ytick.color'] = theme_text
plt.rcParams['grid.color'] = '#f5e6fa'
sns.set_theme(style="whitegrid", rc=plt.rcParams)

# ------------------------------------------------
# Data Loading Function (Simplified)
# ------------------------------------------------
@st.cache_data
def load_data():
    # --- UPDATED DATA URL ---
    DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/main/Insomnic%20.csv"
    df = pd.read_csv(DATA_URL)
    
    # Standardize string columns for consistent plotting
    df['Sex'] = df['Sex'].str.title()
    df['Economic status'] = df['Economic status'].replace({'Satisfy': 'Satisfied', 'Dissatisfy': 'Dissatisfied'})
    
    return df

df = load_data()

# ------------------------------------------------
# Page 2: Score Comparisons
# ------------------------------------------------
st.title("💜 Objective 2: Score Comparisons") 

# --- 1. OBJECTIVE STATEMENT ---
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px; margin-bottom: 1.0em;'>
<h5 style='color:#4a235a; margin-bottom: 0.5em;'>Objective Statement</h5>
<p style='color:#4a235a; margin-bottom:0; font-size: 1.0em;'>
Exploring how depression, insomnia, and addiction scores gently shift across 
different social and academic circles.
</p>
</div>
""", unsafe_allow_html=True)

# --- 2. SUMMARY BOX (100-150 words) ---
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px; border: 1px solid #d63384; margin-bottom: 1.0em;'>
<h4 style='color:#4a235a;'>💬 Objective 2 Summary</h4>
<p style='color:#4a235a; margin-bottom:0;'>
This objective examines how key scores from the cleaned dataset differ across groups. The <b>Addiction Score by Gender</b> boxplot reveals that while both groups have similar medians, female respondents exhibit a wider interquartile range and a slightly higher mean, suggesting greater variability in social media addiction. A more pronounced finding comes from the <b>Depression Score by Economic Status</b> violin plot. The 'Dissatisfied' group not only shows a visibly higher median depression score (PHQ-9) but also a much wider distribution, indicating a greater prevalence of both mild and severe depressive symptoms. Finally, the <b>Average Insomnia Score by Year of Study</b> line plot suggests a concerning trend. Average insomnia scores appear to worsen as academic tenure increases, with a noticeable peak in the 5th and 6th years. This highlights that academic pressure and seniority may be contributing factors to poor sleep quality.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 3. VISUALIZATIONS & INTERPRETATION ---
st.subheader("Visualizations & Interpretation")

# --- V1: Addiction Score by Gender (Boxplot) (UPDATED) ---
st.subheader("Addiction Score by Gender")
fig, ax = plt.subplots()
# Updated to use 'BFAS total' and match Colab parameters
sns.boxplot(data=df, x="Sex", y="BFAS total", hue="Sex", ax=ax, palette="RdPu", legend=False)
ax.set_xlabel("Gender")
ax.set_ylabel("Addiction Score (BFAS)") # Keep friendly label
st.pyplot(fig)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📊 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>This boxplot compares the distribution of addiction scores
between genders. Female respondents show a slightly higher median score
and a wider interquartile range, suggesting more variability in this group.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V2: Depression Score by Economic Status (Violin Plot) (UPDATED) ---
st.subheader("Depression Score by Economic Status")
fig, ax = plt.subplots()
# Updated to use 'Economic status' and 'PHQ-9 total'
sns.violinplot(data=df, x="Economic status", y="PHQ-9 total", ax=ax, inner="quartile", palette="PuRd")
ax.set_xlabel("Economic Status")
ax.set_ylabel("Depression Score (PHQ-9)") # Keep friendly label
st.pyplot(fig)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>🎻 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>The 'Dissatisfied' group not only has a higher median
depression score but also a wider distribution, indicating a greater
prevalence of both mild and severe depressive symptoms compared
to the 'Satisfied' group.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V3: Insomnia Score by Year of Study (Line Plot) (UPDATED) ---
st.subheader("Average Insomnia Score by Year of Study")

try:
    # 'Year Num' is already in Insomnic.csv, but we re-run logic for safety
    df['Year Num'] = df['Year of study'].str.extract('(\d+)').astype(float)
    # Updated to use 'AIS total'
    avg_insomnia = df.groupby('Year of study').agg(
        Mean_Insomnia=('AIS total', 'mean'),
        Year_Num=('Year Num', 'first')
    ).reset_index().sort_values('Year_Num')
    
    fig = px.line(avg_insomnia, x="Year of study", y="Mean_Insomnia", markers=True,
                  labels={"Year of study": "Year of Study", "Mean_Insomnia": "Average Insomnia Score"})
    fig.update_layout(xaxis={'categoryorder':'array', 'categoryarray': avg_insomnia["Year of study"]},
                      paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
    fig.update_traces(line_color=theme_primary)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    <div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📈 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>This line plot shows a noticeable trend where the average
insomnia score appears to increase, peaking around the 5th and 6th years of study.
This may suggest that academic pressure or stress accumulates over time.</p>
</div>
""", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not plot 'Year of study' trend. Error: {e}")
