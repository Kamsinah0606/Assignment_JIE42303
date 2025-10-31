import streamlit as st

# ------------------------------------------------
# Main Page Configuration
# ------------------------------------------------
st.set_page_config(
    page_title="Main Page – TikTok Use Study",
    layout="wide"
)

st.title("The Indirect Effect of TikTok Use on Depressive Symptoms")

st.markdown("""
Welcome to the **Student Survey Dashboard** — exploring:
- TikTok use
- Insomnia
- Depressive symptoms among university students.

---

### 📘 Navigation Guide
Use the sidebar to explore the three study objectives:

1️⃣ **Demographic Distribution**  
2️⃣ **Social Factors vs Addiction**  
3️⃣ **Psychological & Behavioral Trends**

Developed by **NOORHAFIZAH BINTI MUHAMMAD**
Assessment: *Assignment*
Course: *Scientific Visualization (JIE42403)*  
University Malaysia Kelantan
""")

st.image("https://upload.wikimedia.org/wikipedia/en/2/28/TikTok_logo.svg", width=150)
st.success("Select a page from the sidebar to begin exploring.")

