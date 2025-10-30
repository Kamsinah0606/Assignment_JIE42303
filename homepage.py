import streamlit as st

st.set_page_config(
    page_title="The indirect effect of TikTok use on depressive symptoms through insomnia among university students",
    layout="wide"
)

st.header("📊 Scientific Visualization – JIE42303", divider="gray")

st.markdown("""
### 🎓 Research Title
**The indirect effect of TikTok use on depressive symptoms through insomnia among university students**

### 📘 Project Overview
This dashboard presents visual analyses based on a real dataset from **DataBase.xlsx**, 
exploring behavioral and demographic relationships through three main objectives:

1️⃣ **Demographic Distribution**  
2️⃣ **Social Factors vs Addiction**  
3️⃣ **Psychological and Behavioral Trends**

Use the links below to open each objective page.  
Developed by *NOORHAFIZAH BINTI MUHAMMAD*.
""")

st.markdown("---")
st.subheader("🧭 Navigate to Objectives:")

# ✅ Use correct relative paths that include the 'pages/' folder
st.page_link("pages/1_Demographic_Distribution.py", label="📊 Objective 1: Demographic Distribution")
st.page_link("pages/2_Social_Factors_vs_Addiction.py", label="📈 Objective 2: Social Factors vs Addiction")
st.page_link("pages/3_Psychological_Behavioral_Trends.py", label="🧠 Objective 3: Psychological and Behavioral Trends")

st.markdown("---")
st.caption("© 2025 – Scientific Visualization (JIE42303)")
