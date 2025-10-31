import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# ------------------------------------------------
# Global Style Settings
# ------------------------------------------------
sns.set_theme(style="whitegrid")  # nice clean background

st.title("Objective 2 : Social Factors vs Addiction (BFAS Total)")

# ------------------------------------------------
# Load Dataset
# ------------------------------------------------
DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

st.subheader("Objective 2:")
st.info("To examine how social factors such as gender, age, and employment relate to addiction levels (BFAS Total).")

st.markdown("---")

# ------------------------------------------------
# Detect and Assign Colors Automatically for Gender
# ------------------------------------------------
unique_genders = df["Sex"].unique()
base_colors = ["#1f77b4", "#e377c2", "#9467bd", "#2ca02c", "#ff7f0e"]  # blue, pink, purple, green, orange
custom_palette = dict(zip(unique_genders, base_colors[:len(unique_genders)]))

# ------------------------------------------------
# Visualization 4: Boxplot
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(
    x="Sex",
    y="BFAS total",
    data=df,
    ax=ax,
    palette=custom_palette
)
ax.set_title("BFAS Total by Gender", fontsize=12)
ax.set_xlabel("Gender")
ax.set_ylabel("BFAS Total Score")
st.pyplot(fig)

st.markdown("---")

# ------------------------------------------------
# Visualization 5: Scatter Plot
# ------------------------------------------------
fig = px.scatter(
    df,
    x="Age",
    y="BFAS total",
    color="Sex",
    title="Age vs BFAS Total",
    color_discrete_map=custom_palette
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ------------------------------------------------
# Visualization 6: Heatmap
# ------------------------------------------------
pivot = df.pivot_table(index="Employment", columns="Economic status", values="BFAS total", aggfunc="mean")

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(pivot, annot=True, cmap="Purples", ax=ax)
ax.set_title("Mean BFAS by Employment and Economic Status", fontsize=12)
st.pyplot(fig)

# ------------------------------------------------
# Insight Section
# ------------------------------------------------
st.success("Insight: BFAS scores vary across social groups — age and employment type appear linked to behavioral addiction patterns.")
