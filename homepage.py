import streamlit as st

st.set_page_config(
  page_title="The indirect effect of TikTok use on depressive symptoms through insomnia among university students"
)
st.header("Data Visualization",divider="gray")


visualise_1 = st.Page('1_Demographic_Distribution.py', title='Objective 1', icon=":material/school:")
visualise_2 = st.Page('2_Social_Factors_vs_Addiction.py', title = 'Objective 2', icon = ":material/school:")
visualise_3 = st.Page('3_Psychological_Behavioral_Trends.py', title = 'Objective 3', icon = ":material/school:")

home = st.Page('homepage.py', title='Homepage', default=True, icon=":material/home:")

# Assuming you meant to define 'pg' as st.navigation
pg = st.navigation(
    {
        "Menu":[home, visualise_1, visualise_2, visualise_2]
    }
)

pg.run()

st.title("📊 Scientific Visualization – JIE42403")
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
