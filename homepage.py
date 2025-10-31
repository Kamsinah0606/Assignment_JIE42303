import streamlit as st

# ------------------------------------------------
# 🌸 Page Configuration
# ------------------------------------------------
st.set_page_config(
    page_title="TikTok Use and Depressive Symptoms Study",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom sidebar style
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #ffd6e7; /* pastel pink */
        }
        [data-testid="stHeader"] {
            background-color: #fff; /* white header */
        }
        h1, h2, h3 {
            color: #d63384; /* pink headings */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# 🌸 Define Pages
# ------------------------------------------------
objective_1 = st.Page("1_Demographic_Distribution.py",
                      title="Objective 1: Demographic Distribution",
                      icon=":material/analytics:",
                      default=True)

objective_2 = st.Page("2_Social_Factors_vs_Addiction.py",
                      title="Objective 2: Social Factors vs Addiction",
                      icon=":material/groups:")

objective_3 = st.Page("3_Psychological_Behavioral_Trends.py",
                      title="Objective 3: Psychological & Behavioral Trends",
                      icon=":material/psychology:")

# ------------------------------------------------
# 🌸 Navigation Menu
# ------------------------------------------------
pg = st.navigation({
    "Explore the Study": [objective_1, objective_2, objective_3]
})

# ------------------------------------------------
# Run the App
# ------------------------------------------------
pg.run()
