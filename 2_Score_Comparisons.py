import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

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
# Data Loading and Cleaning Function
# ------------------------------------------------
@st.cache_data
def load_data():
    # Use the full DataBase.csv file
    DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
    df = pd.read_csv(DATA_URL)
    
    # --- Data Cleaning and Fixing ---
    sex_mapping = {0: 'Male', 1: 'Female', 2: 'I Do Not Want To Disclose'}
    df['Sex'] = df['Sex01'].map(sex_mapping).fillna(df['Sex'].str.title())
    
    df = df.rename(columns={
        'PHQ-9 total': 'Depression Score',
        'AIS total': 'Insomnia Score',
        'BFAS total': 'Addiction Score',
        'Economic status': 'Economic Status'
    })
    
    employment_mapping = {
        "I don't work and rely on savings or familial support": "Unemployed (Support)",
        "I engage in casual, part-time work": "Part-time Work",
        "I work full-time": "Full-time Work",
        "I don't work and rely on scholarships": "Unemployed (Scholarship)"
    }
    df['Employment'] = df['Employment'].map(employment_mapping).fillna(df['Employment'])
    return df

df = load_data()

# ------------------------------------------------
# Page 2: Score Comparisons
# ------------------------------------------------
st.title("💜 Objective 2: Score Comparisons") 

# --- UPDATED OBJECTIVE BOX ---
# Replaced st.info() with a themed markdown box
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px; margin-bottom: 1.0em;'>
<p style='color:#4a235a; margin-bottom:0; font-size: 1.0em;'>
Exploring how depression, insomnia, and addiction scores gently shift across 
different social and academic circles.
</p>
</div>
""", unsafe_allow_html=True)
# --- END OF UPDATE ---

st.divider()

col1, col2 = st.columns(2)

# --- V1: Addiction Score by Gender (Boxplot) ---
with col1:
    st.subheader("Addiction Score by Gender")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Sex", y="Addiction Score", ax=ax, palette="RdPu")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Addiction Score (BFAS)")
    st.pyplot(fig)
    st.markdown("""
    <div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
    <h5 style='color:#4a235a;'>📊 Summary:</h5>
    <p style='color:#4a235a; margin-bottom:0;'>This boxplot compares the distribution of addiction scores
    between genders. Female respondents show a slightly higher median score
    and a wider interquartile range, suggesting more variability in this group.</p>
    </div>
    """, unsafe_allow_html=True)

# --- V2: Depression Score by Economic Status (Violin Plot) ---
with col2:
    st.subheader("Depression Score by Economic Status")
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x="Economic Status", y="Depression Score", ax=ax, inner="quartile", palette="PuRd")
    ax.set_xlabel("Economic Status")
    ax.set_ylabel("Depression Score (PHQ-9)")
    st.pyplot(fig)
    st.markdown("""
    <div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
    <h5 style='color:#4a235a;'>🎻 Summary:</h5>
    <p style='color:#4a235a; margin-bottom:0;'>The 'Dissatisfied' group not only has a higher median
    depression score but also a wider distribution, indicating a greater
    prevalence of both mild and severe depressive symptoms compared
    to the 'Satisfied' group.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- V3: Insomnia Score by Year of Study (Line Plot) ---
st.subheader("Average Insomnia Score by Year of Study")

try:
    df['Year Num'] = df['Year of study'].str.extract('(\d+)').astype(float)
    avg_insomnia = df.groupby('Year of study').agg(
        Mean_Insomnia=('Insomnia Score', 'mean'),
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
    <h5 style='color:#4a235a;'>📈 Summary:</h5>
    <p style='color:#4a235a; margin-bottom:0;'>This line plot shows a noticeable trend where the average
    insomnia score appears to increase, peaking around the 5th and 6th years of study.
    This may suggest that academic pressure or stress accumulates over time.</p>
    </div>
    """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not plot 'Year of study' trend. Error: {e}")

st.divider()

# --- UPDATED OVERALL SUMMARY BOX ---
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px; border: 1px solid #d63384;'>
<h4 style='color:#4a235a;'>💬 Overall Objective 2 Summary</h4>
<p style='color:#4a235a; margin-bottom:0;'>The analysis reveals clear differences in
psychological scores across social groups. Economic dissatisfaction is strongly
linked to higher depression scores, while addiction levels vary by gender.
Furthermore, insomnia scores appear to worsen in later years of study,
highlighting a potential link between academic progression and sleep quality.</p>
</div>
""", unsafe_allow_html=True)
