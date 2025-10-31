import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(
    page_title="TikTok Use Study – Student Survey",
    layout="wide"
)

# ------------------------------------------------
# Define All Pages (Now includes mainpage)
# ------------------------------------------------
mainpage = st.Page("mainpage.py",
                   title="🏠 Main Page",
                   icon=":material/home:",
                   default=True)  # Start here

objective_1 = st.Page("1_Demographic_Distribution.py",
                      title="📊 Objective 1: Demographic Distribution",
                      icon=":material/analytics:")

objective_2 = st.Page("2_Social_Factors_vs_Addiction.py",
                      title="📈 Objective 2: Social Factors vs Addiction",
                      icon=":material/groups:")

objective_3 = st.Page("3_Psychological_Behavioral_Trends.py",
                      title="🧠 Objective 3: Psychological & Behavioral Trends",
                      icon=":material/psychology:")

# ------------------------------------------------
# Navigation Menu
# ------------------------------------------------
pg = st.navigation({
    "Menu": [mainpage, objective_1, objective_2, objective_3]
})

# ------------------------------------------------
# Run the app
# ------------------------------------------------
pg.run()
