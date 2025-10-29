import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("2️⃣ Social Factors vs Addiction (BFAS Total)")

DATA_URL = "https://raw.githubusercontent.com/<username>/Assignment_JIE42303/main/cleaned_dataset.csv"
df = pd.read_csv(DATA_URL)

st.subheader("Objective:")
st.info("To examine how social factors such as gender, age, and employment relate to addiction levels (BFAS Total).")

# Visualization 4: Boxplot
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(x="Sex", y="BFAS total", data=df, ax=ax)
ax.set_title("BFAS Total by Gender")
st.pyplot(fig)

# Visualization 5: Scatter plot
fig = px.scatter(df, x="Age", y="BFAS total", color="Sex", title="Age vs BFAS Total")
st.plotly_chart(fig, use_container_width=True)

# Visualization 6: Heatmap
pivot = df.pivot_table(index="Employment", columns="Economic status", values="BFAS total", aggfunc="mean")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(pivot, annot=True, cmap="YlGnBu", ax=ax)
ax.set_title("Mean BFAS by Employment and Economic Status")
st.pyplot(fig)

st.success("Insight: BFAS scores vary across social groups — age and employment type appear linked to behavioral addiction patterns.")

