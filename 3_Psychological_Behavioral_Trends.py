import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("3️⃣ Psychological and Behavioral Trends")

DATA_URL = "https://raw.githubusercontent.com/<username>/Assignment_JIE42303/main/cleaned_dataset.csv"
df = pd.read_csv(DATA_URL)

st.subheader("Objective:")
st.info("To explore correlations between psychological factors (AIS) and addiction scores (BFAS Total).")

# Visualization 7: Line plot (AIS vs BFAS)
avg_bfas = df.groupby("AIS 0-1")["BFAS total"].mean().reset_index()
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(x="AIS 0-1", y="BFAS total", data=avg_bfas, marker="o", ax=ax)
ax.set_title("Average BFAS by AIS (0-1)")
st.pyplot(fig)

# Visualization 8: Correlation heatmap
corr = df[["Age", "BFAS total", "Sex01", "AIS 0-1"]].corr()
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Correlation Matrix (Selected Variables)")
st.pyplot(fig)

# Visualization 9: 3D scatter plot
fig = px.scatter_3d(df, x="Age", y="BFAS total", z="AIS 0-1", color="Sex", title="3D Relationship: Age, BFAS, AIS")
st.plotly_chart(fig, use_container_width=True)

st.success("Insight: AIS scores positively correlate with BFAS totals, suggesting higher internet use is linked to addiction intensity.")

