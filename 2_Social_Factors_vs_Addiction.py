import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set global Seaborn theme
sns.set_theme(style="whitegrid", palette="viridis")  # or "pastel", "deep", "coolwarm", etc.

st.title("Objective 2 : Social Factors vs Addiction (BFAS Total)")

DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

st.subheader("Objective 2:")
st.info("To examine how social factors such as gender, age, and employment relate to addiction levels (BFAS Total).")

st.markdown("---")

# Visualization 4: Boxplot
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(x="Sex", y="BFAS total", data=df, ax=ax)
ax.set_title("BFAS Total by Gender")
st.pyplot(fig)

st.markdown("---")

# Visualization 5: Scatter plot
fig = px.scatter(df, x="Age", y="BFAS total", color="Sex", title="Age vs BFAS Total", color_discrete_sequence=["#9b59b6", "#8e44ad"])
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Visualization 6: Heatmap
pivot = df.pivot_table(index="Employment", columns="Economic status", values="BFAS total", aggfunc="mean")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(pivot, annot=True, cmap="Purples", ax=ax)
ax.set_title("Mean BFAS by Employment and Economic Status")
st.pyplot(fig)

st.success("Insight: BFAS scores vary across social groups — age and employment type appear linked to behavioral addiction patterns.")
