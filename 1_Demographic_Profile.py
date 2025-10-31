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
plt.rcParams['grid.color'] = '#f5e6fa' # Light purple grid
sns.set_theme(style="whitegrid", rc=plt.rcParams)

# ------------------------------------------------
# Data Loading and Cleaning Function
# ------------------------------------------------
@st.cache_data
def load_data():
    DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/Insomnic%20.csv"
    df = pd.read_csv(DATA_URL)
    
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
# Page 1: Demographic Profile
# ------------------------------------------------
st.title("Objective 1: Demographic Profile")

# --- 1. OBJECTIVE STATEMENT (WITH TITLE) ---
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px; margin-bottom: 1.0em;'>
<h5 style='color:#4a235a; margin-bottom: 0.5em;'>Objective Statement</h5>
<p style='color:#4a235a; margin-bottom:0; font-size: 1.0em;'>
A closer look at the demographic, economic, and academic profile of our survey respondents.
</p>
</div>
""", unsafe_allow_html=True)
# --- END OF UPDATE ---

# --- 2. SUMMARY BOX (100-150 words) ---
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px; border: 1px solid #d63384; margin-bottom: 1.0em;'>
<h4 style='color:#4a235a;'>Summary Box</h4>
<p style='color:#4a235a; margin-bottom:0;'>
This page profiles the 173 survey respondents. The <b>Age Distribution</b> histogram confirms the sample aligns with the target population, showing a high concentration of young adults between 20-25. The <b>Gender Distribution</b> pie chart reveals a relatively balanced cohort, with female respondents (59.5%) slightly outnumbering male respondents (39.9%). The <b>Employment vs. Economic Status</b> grouped bar chart provides key context: the vast majority of participants are 'Unemployed (Support),' which is typical for full-time students. Within this group, most report a 'Satisfied' economic status. Finally, the <b>Field of Study</b> bar chart highlights the academic diversity of the sample, with 'Pharmacy' (23.1%) and 'Psychology' (17.9%) being the most common fields. Overall, the demographic baseline is a young, balanced, and academically varied student body.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 3. VISUALIZATIONS & INTERPRETATION ---
st.subheader("Visualizations & Interpretation")

st.divider()

# --- V1: Age Distribution (Histogram) ---
st.subheader("Age Distribution of Respondents")
fig, ax = plt.subplots()
sns.histplot(df["Age"], bins=10, kde=True, ax=ax, color=theme_primary)
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")
st.pyplot(fig)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>The histogram shows that the majority of respondents are young adults,
primarily concentrated between 20 and 25 years old. This aligns with the target
population of university students.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V2: Gender Distribution (Pie Chart) ---
st.subheader("Gender Distribution")
gender_counts = df["Sex"].value_counts().reset_index()
gender_counts.columns = ['Sex', 'Count']
fig = px.pie(gender_counts, values='Count', names='Sex', 
             title="Respondent Gender", hole=0.3,
             color_discrete_sequence=["#d63384", "#8a4baf", "#f5e6fa"]) 
fig.update_layout(paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
st.plotly_chart(fig, use_container_width=True)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>The gender ratio is relatively balanced, with a slightly higher
proportion of female respondents (59.5% vs 39.9%). This ensures that the analysis can provide
representative insights across genders.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V3: Employment vs. Economic Status (Grouped Bar) ---
st.subheader("Employment vs. Economic Status")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x="Employment", hue="Economic Status", ax=ax, palette="RdPu")
ax.set_xlabel("Employment Status")
ax.set_ylabel("Count")
ax.tick_params(axis='x', rotation=15)
plt.legend(title="Economic Status")
st.pyplot(fig)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>Most respondents are unemployed and rely on support, and within this
group, the majority report a "Satisfied" economic status. This is typical for
a student population.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V4: Field of Study (Bar Chart) ---
st.subheader("Respondents by Field of Study")
study_counts = df["Field of study"].value_counts(normalize=True).head(10).reset_index()
study_counts.columns = ['Field', 'Percentage']
study_counts['Percentage'] = (study_counts['Percentage'] * 100).round(1)

fig = px.bar(study_counts, x='Percentage', y='Field', orientation='h',
             title="Top 10 Fields of Study",
             text='Percentage',
             color_discrete_sequence=[theme_primary]) 
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(yaxis={'categoryorder':'total ascending'},
                  paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
st.plotly_chart(fig, use_container_width=True)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>This chart shows the academic diversity of the sample.
'Pharmacy' (23.1%) and 'Psychology' (17.9%) are the most represented fields in this dataset.</p>
</div>
""", unsafe_allow_html=True)
