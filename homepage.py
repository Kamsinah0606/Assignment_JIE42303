import streamlit as st

st.set_page_config(
  page_title="The indirect effect of TikTok use on depressive symptoms through insomnia among university students"
)
st.header("Data Visualization - JIE42303",divider="gray")

st.markdown("""
Welcome to my scientific visualization dashboard!

This project presents data analysis based on a real dataset from **DataBase.xlsx**, 
exploring behavioral and demographic relationships through three objectives:
1. **Demographic Distribution**
2. **Social Factors vs Addiction**
3. **Psychological and Behavioral Trends**

Use the sidebar or page tabs to explore the visuals.  
Developed by *NOORHAFIZAH BINTI MUHAMMAD*.
""")

# Navigation Buttons
st.markdown("---")
st.subheader(" Navigate to Objectives:")
st.page_link('pages/1_Demographic_Distribution.py', title='Objective 1: Demographic Distribution', icon=":material/school:")
st.page_link('pages/2_Social_Factors_vs_Addiction.py', title = 'Objective 2: Social Factors vs Addiction', icon = ":material/school:")
st.page_link('pages/3_Psychological_Behavioral_Trends.py', title = 'Objective 3: Psychological and Behavioral Trends ', icon = ":material/school:")

home = st.Page('homepage.py', title='Homepage', default=True, icon=":material/home:")
)

pg.run()
