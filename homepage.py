import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="The indirect effect of TikTok use on depressive symptoms through insomnia among university students",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"

try:
    df = pd.read_csv(DATA_URL, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(DATA_URL, encoding="ISO-8859-1", errors="replace")

# -----------------------------
# Header
# -----------------------------
st.title("📊 Scientific Visualization – JIE42303")
st.write("""
### 🎓 Research Title

**The indirect effect of TikTok use on depressive symptoms through insomnia among university students**

This dashboard presents three visualization objectives:

1️⃣ Demographic Distribution  
2️⃣ Social Factors vs Addiction  
3️⃣ Psychological and Behavioral Trends
""")

# -----------------------------
# Navigation Menu
# -----------------------------
pg = st.navigation({
    "Menu": ["Objective 1","Objective 2","Objective 3"]
                   })

# -------------------------------
# Define all pages
# -------------------------------
pages_1 = st.Page(
    "1_Demographic_Distribution.py",
    title="Objective 1",
    icon=":material/analytics:",
    default=True
)

pages_2 = st.Page(
    "2_Social_Factors_vs_Addiction.py",
    title="Objective 2",
    icon=":material/analytics:"
)

pages_3 = st.Page(
    "3_Psychological_Behavioral_Trends.py",
    title="Objective 3",
    icon=":material/groups:"
)

# -----------------------------
# Objective 1
# -----------------------------
if "Objective 1" in page:
    st.header("📊 Objective 1: Demographic Distribution")
    st.info("Analyze demographic distribution of respondents by age, gender, and employment type.")

    # Age distribution
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(df["Age"], bins=10, kde=True, ax=ax)
    ax.set_title("Age Distribution of Respondents")
    st.pyplot(fig)

    # Gender ratio
    gender_counts = df["Sex"].value_counts()
    fig, ax = plt.subplots(figsize=(5,5))
    ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Gender Ratio")
    st.pyplot(fig)

    # Employment
    fig, ax = plt.subplots(figsize=(8,4))
    sns.countplot(y="Employment", data=df, order=df["Employment"].value_counts().index, ax=ax)
    ax.set_title("Employment Distribution")
    st.pyplot(fig)

# -----------------------------
# Objective 2
# -----------------------------
elif "Objective 2" in page:
    st.header("📈 Objective 2: Social Factors vs Addiction (BFAS Total)")
    st.info("Examine how social factors like gender, age, and employment relate to addiction levels (BFAS Total).")

    # Boxplot
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x="Sex", y="BFAS total", data=df, ax=ax)
    ax.set_title("BFAS Total by Gender")
    st.pyplot(fig)

    # Scatter
    fig = px.scatter(df, x="Age", y="BFAS total", color="Sex", title="Age vs BFAS Total")
    st.plotly_chart(fig, use_container_width=True)

    # Heatmap
    pivot = df.pivot_table(index="Employment", columns="Economic status", values="BFAS total", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.heatmap(pivot, annot=True, cmap="YlGnBu", ax=ax)
    ax.set_title("Mean BFAS by Employment and Economic Status")
    st.pyplot(fig)

# -----------------------------
# Objective 3
# -----------------------------
else:
    st.header("🧠 Objective 3: Psychological and Behavioral Trends")
    st.info("Explore correlations between psychological factors (AIS) and addiction scores (BFAS Total).")

    # Line plot
    avg_bfas = df.groupby("AIS 0-1")["BFAS total"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6,4))
    sns.lineplot(x="AIS 0-1", y="BFAS total", data=avg_bfas, marker="o", ax=ax)
    ax.set_title("Average BFAS by AIS (0-1)")
    st.pyplot(fig)

    # Correlation heatmap
    corr = df[["Age", "BFAS total", "AIS 0-1"]].corr()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap (Age, BFAS total, AIS 0-1)")
    st.pyplot(fig)

    # 3D Scatter
    fig = px.scatter_3d(df, x="Age", y="BFAS total", z="AIS 0-1", color="Sex",
                        title="3D Relationship: Age, BFAS, AIS")
    st.plotly_chart(fig, use_container_width=True)
