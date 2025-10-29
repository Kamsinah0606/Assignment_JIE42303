import streamlit as st

st.set_page_config(
  page_title="The indirect effect of TikTok use on depressive symptoms through insomnia among university students"
)
st.header("Data Visualization",divider="gray")
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
# Navigation buttons
st.markdown("---")
col1, col2 = st.columns([1, 3])
with col1:
    st.page_link("pages/1_Demographic_Distribution.py", label="➡ Go to Objective 1", icon="📊")

