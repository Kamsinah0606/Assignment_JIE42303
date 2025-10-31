import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# ------------------------------------------------
# Data Loading and Cleaning Function
# ------------------------------------------------
@st.cache_data
def load_data():
    DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase_Preprocessed.csv"
    df = pd.read_csv(DATA_URL)
    
    # --- Data Cleaning and Fixing ---
    # Fix the 'Sex' column by mapping 'Sex01'
    # This was the cause of your original KeyError
    sex_mapping = {0: 'Male', 1: 'Female', 2: 'I Do Not Want To Disclose'}
    df['Sex'] = df['Sex01'].map(sex_mapping).fillna('Unknown')
    
    # Rename key columns for clarity in plots
    df = df.rename(columns={
        'PHQ-9 total': 'Depression Score',
        'AIS total': 'Insomnia Score',
        'BFAS total': 'Addiction Score',
        'Economic status': 'Economic Status' # Fix spacing
    })
    
    # Shorten 'Employment' for plots
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
st.title("👤 Objective 1: Demographic Profile")
st.info("To analyze the demographic, economic, and academic distribution of the survey respondents.")
st.divider()

# --- Layout ---
col1, col2 = st.columns([1, 1])

# --- V1: Age Distribution (Histogram) ---
with col1:
    st.subheader("Age Distribution of Respondents")
    fig, ax = plt.subplots()
    sns.histplot(df["Age"], bins=10, kde=True, ax=ax)
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    st.markdown("""
    **Summary:** The histogram shows that the majority of respondents are young adults,
    primarily concentrated between 20 and 25 years old. This aligns with the target
    population of university students.
    """)

# --- V2: Gender Distribution (Pie Chart) ---
with col2:
    st.subheader("Gender Distribution")
    gender_counts = df["Sex"].value_counts().reset_index()
    gender_counts.columns = ['Sex', 'Count']
    fig = px.pie(gender_counts, values='Count', names='Sex', 
                 title="Respondent Gender", hole=0.3)
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    **Summary:** The gender ratio is relatively balanced, with a slightly higher
    proportion of female respondents. This ensures that the analysis can provide
    representative insights across genders.
    """)

st.divider()

# --- Layout ---
col3, col4 = st.columns([2, 1])

# --- V3: Employment vs. Economic Status (Grouped Bar) ---
with col3:
    st.subheader("Employment vs. Economic Status")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x="Employment", hue="Economic Status", ax=ax, palette="Blues_r")
    ax.set_xlabel("Employment Status")
    ax.set_ylabel("Count")
    ax.tick_params(axis='x', rotation=15)
    plt.legend(title="Economic Status")
    st.pyplot(fig)
    st.markdown("""
    **Summary:** Most respondents are unemployed and rely on support, and within this
    group, the majority report a "Satisfied" economic status. This is typical for
    a student population.
    """)

# --- V4: Field of Study (Bar Chart) ---
with col4:
    st.subheader("Respondents by Field of Study")
    study_counts = df["Field of study"].value_counts().head(10).reset_index()
    study_counts.columns = ['Field', 'Count']
    fig = px.bar(study_counts, x='Count', y='Field', orientation='h',
                 title="Top 10 Fields of Study")
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    **Summary:** This chart shows the academic diversity of the sample,
    highlighting the most common fields of study.
    """)

st.divider()
st.success("""
**🌼 Overall Objective 1 Summary:** The dataset represents a young, academically diverse
university population with a balanced gender ratio. Most are students who are
economically satisfied, providing a stable baseline for analyzing the
psychological and behavioral factors in the following objectives.
""")
