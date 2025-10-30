import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(
    page_title="The indirect effect of TikTok use on depressive symptoms through insomnia among university students",
    layout="wide"
)

# ------------------------------------------------
# Define Pages (only 3 objectives — no homepage page)
# ------------------------------------------------
objective_1 = st.Page("1_Demographic_Distribution.py",
                      title="📊 Objective 1: Demographic Distribution",
                      icon=":material/analytics:",
                      default=True)  # start here

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
    "Menu": [objective_1, objective_2, objective_3]
})

# ------------------------------------------------
# Run the app
# ------------------------------------------------
pg.run()
