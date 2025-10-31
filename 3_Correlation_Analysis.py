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
theme_purple = "#8a4baf"

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
    DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase_Preprocessed.csv"
    df = pd.read_csv(DATA_URL)
    
    # --- Data Cleaning and Fixing ---
    sex_mapping = {0: 'Male', 1: 'Female', 2: 'I Do Not Want To Disclose'}
    df['Sex'] = df['Sex01'].map(sex_mapping).fillna('Unknown')
    
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
# Page 3: Correlation Analysis
# ------------------------------------------------
st.title("💖 Objective 3: Correlation Analysis") # Added emoji
st.info("To investigate the relationships between the key psychological and behavioral scores.")
st.divider()

# --- Layout ---
col1, col2 = st.columns(2)

# --- V1: Insomnia vs. Depression (Scatter Plot) ---
with col1:
    st.subheader("Insomnia Score vs. Depression Score")
    # Updated trendline color
    fig = px.scatter(df, x="Insomnia Score", y="Depression Score", 
                     trendline="ols", trendline_color_override=theme_primary,
                     title="Strong Positive Correlation",
                     color_discrete_sequence=[theme_purple]) # Updated dot color
    # Updated background
    fig.update_layout(xaxis_title="Insomnia Score (AIS)", yaxis_title="Depression Score (PHQ-9)",
                      paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    **Summary:** This plot reveals a strong, positive linear relationship. As
    Insomnia Scores increase, Depression Scores tend to increase as well. The
    tight clustering around the trendline suggests a powerful link between
    poor sleep and depressive symptoms.
    """)

# --- V2: Addiction vs. Insomnia (Scatter Plot) ---
with col2:
    st.subheader("Addiction Score vs. Insomnia Score")
    # Added theme-based color map for gender
    color_map = {"Male": theme_purple, "Female": theme_primary, "I Do Not Want To Disclose": "#bfa0c6"}
    fig = px.scatter(df, x="Insomnia Score", y="Addiction Score", color="Sex",
                     trendline="ols", title="Moderate Positive Correlation by Gender",
                     color_discrete_map=color_map)
    # Updated background
    fig.update_layout(xaxis_title="Insomnia Score (AIS)", yaxis_title="Addiction Score (BFAS)",
                      paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    **Summary:** A moderate positive correlation is also visible here. Higher
    insomnia is linked to higher addiction scores. By coloring for gender,
    we can observe that the relationship holds for all groups, though
    females (pink) are more represented in the high-score quadrant.
    """)

st.divider()

# --- V3: Correlation Heatmap ---
st.subheader("Correlation Matrix of Key Variables")
corr_cols = ['Depression Score', 'Insomnia Score', 'Addiction Score', 'Age', 'Sex01']
corr_matrix = df[corr_cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
# Updated heatmap color map (cmap) to match theme
sns.heatmap(corr_matrix, annot=True, cmap="RdPu", center=0, fmt=".2f",
            linewidths=.5, ax=ax)
ax.set_title("Heatmap of Numeric Correlations")
st.pyplot(fig)
st.markdown("""
**Summary:** The heatmap provides a powerful summary.
- **Insomnia & Depression (0.64):** Confirms the strong positive correlation seen in the scatter plot.
- **Insomnia & Addiction (0.42):** Confirms the moderate positive correlation.
- **Age:** Age shows a slight negative correlation with all three scores,
suggesting that older students in this sample tended to report slightly
better mental health and lower addiction.
""")

st.divider()
st.success("""
**🧠 Overall Objective 3 Summary:** The findings strongly indicate that these
conditions are highly interconnected. The most significant relationship is
between insomnia and depression, suggesting a co-aggravating cycle.
Social media addiction is also part of this negative cluster,
correlating with both poor sleep and depression. This highlights a
critical interplay between sleep, mental health, and digital behavior.
""")
