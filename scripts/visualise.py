# scripts/visualize.py

import pandas as pd
import plotly.express as px
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Streamlit setup
st.set_page_config(layout="wide")
st.title("📌 Campaign Issue Crystallizer — Visual Explorer")

# --- Load Data with Caching ---
@st.cache_data
def load_data():
    cleaned = pd.read_csv("./Project_July/data/cleaned_posts.csv")
    planks = pd.read_csv("./Project_July/data/platform_planks.csv")
    return cleaned, planks

cleaned_df, planks_df = load_data()

# --- Section 1: Issue Frequency Bar Chart ---
st.header("1. 🗳️ Most Discussed Issues")
issue_counts = cleaned_df["issue_category"].value_counts().reset_index()
issue_counts.columns = ["Issue Category", "Number of Posts"]

fig1 = px.bar(
    issue_counts,
    x="Issue Category",
    y="Number of Posts",
    color="Issue Category",
    title="Frequency of Local Issues on r/pittsburgh",
)
st.plotly_chart(fig1, use_container_width=True)

# --- Section 2: Word Cloud ---
st.header("2. 🔤 Word Cloud (Optional)")
if "clean_text" in cleaned_df.columns:
    text = " ".join(cleaned_df["clean_text"].dropna().tolist())
    wordcloud = WordCloud(width=800, height=300, background_color='white').generate(text)

    fig2, ax = plt.subplots(figsize=(10, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig2)
else:
    st.warning("🛑 'clean_text' column not found in dataset. Word Cloud skipped.")

# --- Section 3: Issue Drilldown ---
st.header("3. 🔍 Explore by Issue Category")
selected_issue = st.selectbox("Choose an issue category", cleaned_df["issue_category"].unique())

filtered = cleaned_df[cleaned_df["issue_category"] == selected_issue]
st.markdown(f"### Showing {len(filtered)} posts about **{selected_issue}**")
st.dataframe(filtered[["title", "full_text", "score", "num_comments"]])

# --- Section 4: View Platform Planks ---
st.header("4. 🧱 Platform Planks")
if not planks_df.empty:
    for index, row in planks_df.iterrows():
        with st.expander(f"📌 {row['issue_category']}"):
            st.markdown(f"```\n{row['platform_plank']}\n```")
else:
    st.warning("No platform planks found.")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ by Kriti | Carnegie Mellon University | July 2025")
