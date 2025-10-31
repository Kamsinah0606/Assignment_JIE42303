import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

sns.set_theme(style="whitegrid", palette="mako")

st.title("💜 Objective 2: Social Factors vs Addiction (BFAS Total)")
st.info("To examine how social factors such as gender, age, and employment relate to addiction levels (BFAS Total).")

DATA_URL = "https://raw.githubusercontent.com/Kamsinah0606/Assignment_JIE42303/refs/heads/main/DataBase.csv"
df = pd.read_csv(DATA_URL)

st.divider()

# Visualization 4: Boxplot by Gender
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(
    x="Sex", y="BFAS total", data=df, ax=ax,
    palette={"Male": "#6a5acd", "Female": "#ff80ab", "I do not want to disclose": "#b39ddb"}
)
ax.set_title("BFAS Total by Gender")
st.pyplot(fig)

# Visualization 5: Scatter plot (Age vs BFAS)
st.divider()
fig = px.scatter(
    df, x="Age", y="BFAS total", color="Sex",
    title="Age vs BFAS Total",
    color_discrete_map={
        "Female": "#ff80ab",
        "Male": "#6a5acd",
        "I do not want to disclose": "#b39ddb"
    }
)
st.plotly_chart(fig, use_container_width=True)

# Visualization 6: Heatmap (Employment vs Economic Status)
st.divider()
pivot = df.pivot_table(index="Employment", columns="Economic status", values="BFAS total", aggfunc="mean")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(pivot, annot=True, cmap="RdPu", ax=ax)
ax.set_title("Mean BFAS by Employment and Economic Status")
st.pyplot(fig)

# Summary Box
st.markdown("""
<div style='background-color:#f5e6fa; padding:20px; border-radius:15px;'>
  <h4 style='color:#4a235a;'>💬 Summary Insight</h4>
  <p style='color:#4a235a;'>
  BFAS scores vary across social groups. Gender and employment type influence addiction levels, 
  suggesting that social and lifestyle factors play a key role in behavioral engagement patterns.
  </p>
</div>
""", unsafe_allow_html=True)
