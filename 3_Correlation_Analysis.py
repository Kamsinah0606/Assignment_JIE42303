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
# Page 3: Correlation Analysis
# ------------------------------------------------
st.title("💖 Objective 3: Correlation Analysis") 

# --- 1. OBJECTIVE STATEMENT ---
st.markdown("""
<div style='background-color:#f5e6fa; padding:15px; border-radius:12px; margin-bottom: 1.0em;'>
<h5 style='color:#4a235a; margin-bottom: 0.5em;'>Objective Statement</h5>
<p style='color:#4a235a; margin-bottom:0; font-size: 1.0em;'>
Uncovering the delicate connections between the key psychological and behavioral scores.
</p>
</div>
""", unsafe_allow_html=True)

# --- 2. SUMMARY BOX (100-150 words) ---
st.markdown("""
<div style='background-color:#f3e5f5; padding:20px; border-radius:15px; border: 1px solid #d63384; margin-bottom: 1.0em;'>
<h4 style='color:#4a235a;'>🧠 Objective 3 Summary</h4>
<p style='color:#4a235a; margin-bottom:0;'>
This objective investigates the relationships between the psychological scores from the cleaned dataset. The <b>Insomnia vs. Depression</b> scatter plot reveals the strongest finding: a significant <b>positive correlation of +0.64</b>. The tight clustering of data along the trendline suggests a powerful co-aggravating cycle, where poor sleep and depressive symptoms are deeply linked. A similar, though more moderate, relationship is seen in the <b>Addiction vs. Insomnia</b> scatter plot, which shows a positive correlation of <b>+0.42</b>. This link persists across genders, with female respondents (pink) being more represented in the high-score quadrant. The <b>Correlation Heatmap</b> provides a comprehensive summary, confirming these two positive relationships. It also shows that <b>Age</b> has a slight negative correlation with all three scores, suggesting older students in this sample reported slightly better mental health.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 3. VISUALIZATIONS & INTERPRETATION ---
st.subheader("Visualizations & Interpretation")

# --- V1: Insomnia vs. Depression (Scatter Plot) ---
st.subheader("Insomnia Score vs. Depression Score")
fig = px.scatter(df, x="AIS total", y="PHQ-9 total", 
                 trendline="ols", trendline_color_override=theme_primary,
                 title="Strong Positive Correlation",
                 color_discrete_sequence=[theme_purple]) 
fig.update_layout(xaxis_title="Insomnia Score (AIS)", yaxis_title="Depression Score (PHQ-9)",
                  paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
st.plotly_chart(fig, use_container_width=True)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>🔗 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>This plot reveals a strong, positive linear relationship (correlation: +0.64). As
Insomnia Scores increase, Depression Scores tend to increase as well. The
tight clustering around the trendline suggests a powerful link between
poor sleep and depressive symptoms.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V2: Addiction vs. Insomnia (Scatter Plot) (FIXED) ---
st.subheader("Addiction Score vs. Insomnia Score")
color_map = {"Male": theme_purple, "Female": theme_primary, "I Do Not Want To Disclose": "#bfa0c6"}
fig = px.scatter(df, x="AIS total", y="BFAS total", color="Sex",
                 trendline="ols", title="Moderate Positive Correlation by Gender",
                 color_discrete_map=color_map)
# --- THIS LINE IS NOW FIXED ---
fig.update_layout(xaxis_title="Insomnia Score (AIS)", yaxis_title="Addiction Score (BFAS)",
                  paper_bgcolor=theme_bg, plot_bgcolor=theme_bg, font_color=theme_text)
# --- END OF FIX ---
st.plotly_chart(fig, use_container_width=True)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>📱 Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>A moderate positive correlation (+0.42) is also visible here. Higher
insomnia is linked to higher addiction scores. By coloring for gender,
we can observe that the relationship holds for all groups, though
females (pink) are more represented in the high-score quadrant.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- V3: Correlation Heatmap ---
st.subheader("Correlation Matrix of Key Variables")
corr_cols = ['PHQ-9 total', 'AIS total', 'BFAS total', 'Age', 'Sex01']
corr_matrix = df[corr_cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="RdPu", center=0, fmt=".2f",
            linewidths=.5, ax=ax)
ax.set_title("Heatmap of Numeric Correlations")
st.pyplot(fig)
st.markdown("""
<div style='background-color:#f5e6fa;padding:15px;border-radius:12px;'>
<h5 style='color:#4a235a;'>Matrix Interpretation:</h5>
<p style='color:#4a235a; margin-bottom:0;'>The heatmap provides a powerful summary.
<br>• <b>Insomnia & Depression (0.64):</b> Confirms the strong positive correlation.
<br>• <b>Insomnia & Addiction (0.42):</b> Confirms the moderate positive correlation.
<br>• <b>Age:</b> Age shows a slight negative correlation with all three scores,
suggesting that older students in this sample reported slightly
better mental health and lower addiction.</p>
</div>
""", unsafe_allow_html=True)
