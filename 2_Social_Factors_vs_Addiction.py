import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

# Theme
sns.set_theme(style="whitegrid", palette="pink")

st.title("📈 Objective 2: Social Factors vs Addiction (BFAS Total)")
st.info("To examine how social factors such as gender, age, and economic background relate to addiction levels (BFAS Total).")

st.divider()

# Color map
unique_genders = df["Sex"].unique()
custom_palette = dict(zip(unique_genders, ["#ff5c8d", "#ff9ecd", "#b56576"]))

# Visualization 4: Boxplot (BFAS by Gender)
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(x="Sex", y="BFAS total", data=df, ax=ax, palette=custom_palette)
ax.set_title("BFAS Total by Gender", color="#d63384")
st.pyplot(fig)

st.divider()

# Visualization 5: Scatter (Age vs BFAS)
fig = px.scatter(
    df,
    x="Age",
    y="BFAS total",
    color="Sex",
    color_discrete_map=custom_palette,
    title="Age vs BFAS Total by Gender"
)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# Visualization 6: Violin Plot (Economic status vs BFAS)
fig, ax = plt.subplots(figsize=(7,5))
sns.violinplot(x="Economic status", y="BFAS total", data=df, ax=ax, palette="pink")
ax.set_title("BFAS Distribution by Economic Status", color="#d63384")
st.pyplot(fig)

st.success("Insight: Female respondents and those with higher economic stability show slightly higher BFAS scores, indicating that social and economic factors may influence behavioral addiction levels.")
