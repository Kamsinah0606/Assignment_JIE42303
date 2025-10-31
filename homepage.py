import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(
    page_title="Student Mental Health & Addiction Analysis",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------
# Define Pages
# ------------------------------------------------
objective_1 = st.Page(
    "1_Demographic_Profile.py",
    title="Objective 1: Demographic Profile",
    icon=":material/analytics:",
    default=True
)

objective_2 = st.Page(
    "2_Score_Comparisons.py",
    title="Objective 2: Score Comparisons",
    icon=":material/compare_arrows:"
)

objective_3 = st.Page(
    "3_Correlation_Analysis.py",
    title="Objective 3: Correlation Analysis",
    icon=":material/query_stats:"
)

# ------------------------------------------------
# Navigation Menu
# ------------------------------------------------
pg = st.navigation({
    "Menu": [objective_1, objective_2, objective_3]
})

st.set_option('deprecation.showPyplotGlobalUse', False)
pg.run()
