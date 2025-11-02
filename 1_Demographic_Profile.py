import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# ------------------------------------------------
# THEME & PLOT SETTINGS
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
# LOAD DATA FUNCTION
# ------------------------------------------------
@st.cache_data
def load_data():
    DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/main/Insomnic%20.csv"
    df = pd.read_csv(DATA_URL)
    df['Sex'] = df['Sex'].str.title()
    df['Economic status'] = df['Economic status'].replace({'Satisfy': 'Satisfied', 'Dissatisfy': 'Dissatisfied'})
    return df

df = load_data()

# ------------------------------------------------
# PAGE 1: DEMOGRAPHIC PROFILE
# ------------------------------------------------
st.title("🌸 Objective 1: Demographic Profile")

# ---- METRIC CARDS ----
total_respondents = len(df)
avg_age = df['Age'].mean()
avg_depression = df['PHQ-9 total'].mean()
avg_insomnia = df['AIS total'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Total Respondents", value=total_respondents)
col2.metric(label="Average Age", value=f"{avg_age:.1f}")
col3.metric(label="Avg. Depression Score", value=f"{avg_depression:.1f}")
col4.metric(label="Avg. Insomnia Score", value=f"{avg_insomnia:.1f}")

# ------------------------------------------------
# OBJECTIVE STATEMENT
# ------------------------------------------------
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px; margin-bottom: 1.0em;'>
<h5 style='color:#4a235a; margin-bottom: 0.5em;'>Objective Statement</h5>
<p style='color:#4a235a; margin-bottom:0; font-size: 1.0em;'>
To describe the demographic and academic characteristics of the respondents, 
focusing on age distribution, gender representation, economic satisfaction, 
and field of study.
</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# UPDATED SUMMARY BOX (100–150 WORDS)
# ------------------------------------------------
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px; border: 1px solid #d63384; margin-bottom: 1.0em;'>
<h4 style='color:#4a235a;'>🌼 Objective 1 Summary</h4>
<p style='color:#4a235a; margin-bottom:0;'>
The demographic analysis was conducted to provide an overview of the respondents’ 
age, gender, and academic background. It was found that most participants were young adults 
aged between 20 and 25 years old, representing the typical age range of university students. 
The gender distribution showed that female respondents formed the majority, followed by male participants, 
while one respondent preferred not to disclose their gender. This distribution demonstrated inclusivity 
and balance in the dataset. In addition, the majority of respondents were observed to be economically satisfied 
and not formally employed, which is consistent with the lifestyle of full-time students. 
The field of study analysis indicated that participants came from various academic disciplines, 
with pharmacy and psychology being the most represented fields.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# VISUALIZATIONS & INTERPRETATIONS
# ------------------------------------------------
st.subheader("Visualizations & Interpretation")

# --- V1: AGE DISTRIBUTION ---
st.subheader("Age Distribution of Respondents")
fig, ax = plt.subplots()
sns.histplot(df["Age"], bins=10, kde=True, ax=ax, color=theme_primary)
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📊 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>
The histogram showed that most respondents were between 20 and 25 years old, 
indicating that the sample mainly consisted of young adults. 
The distribution was slightly right-skewed, with fewer respondents above 25 years of age. 
This trend was consistent with the expected age characteristics of university students.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V2: GENDER DISTRIBUTION ---
st.subheader("Gender Distribution")
gender_counts = df["Sex"].value_counts().reset_index()
gender_counts.columns = ['Sex', 'Count']

fig = px.pie(
    gender_counts,
    values='Count',
    names='Sex',
    title="Respondent Gender",
    hole=0.3,
    color_discrete_sequence=["#d63384", "#8a4baf", "#f5e6fa"]
)
fig.update_layout(paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>💬 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>
The pie chart illustrated three gender categories: Female, Male, and 
“I do not want to disclose.” Female respondents represented the largest portion of the sample, 
followed by males, while one participant chose not to disclose their gender. 
This distribution indicated that the dataset was slightly female-dominant while maintaining 
gender inclusivity. The small proportion of undisclosed gender was noted as a positive reflection 
of participant privacy awareness.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V3: ECONOMIC VS EMPLOYMENT STATUS ---
st.subheader("Economic vs. Employment Status")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x="Economic status", hue="Employment_Simplified", ax=ax, palette="RdPu")
ax.set_title("Economic Status vs. Employment Status")
ax.set_xlabel("Economic Status")
ax.set_ylabel("Count")
plt.legend(title="Employment Status (Simplified)")
st.pyplot(fig)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📈 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>
The bar chart showed the distribution of students’ economic satisfaction by employment status. 
It was found that the majority of respondents were economically satisfied and categorized under 
unemployed or supported students (A). This pattern reflected the characteristics of a population 
composed mainly of full-time students with limited formal employment. The findings also suggested 
that financial satisfaction was not necessarily dependent on having employment within this group.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V4: FIELD OF STUDY ---
st.subheader("Respondents by Field of Study")
study_counts = df["Field of study"].value_counts(normalize=True).head(10).reset_index()
study_counts.columns = ['Field', 'Percentage']
study_counts['Percentage'] = (study_counts['Percentage'] * 100).round(1)

fig = px.bar(study_counts, x='Percentage', y='Field', orientation='h',
             title="Top 10 Fields of Study",
             text='Percentage',
             color_discrete_sequence=[theme_primary])
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(yaxis={'categoryorder': 'total ascending'},
                  paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>🎓 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>
The bar chart showed the academic diversity of the sample. 
The highest proportion of respondents was from the pharmacy field, followed by psychology. 
This indicated that the dataset was composed primarily of students from health and behavioral 
science backgrounds, providing valuable context for subsequent mental health analyses.
</p>
</div>
""", unsafe_allow_html=True)
