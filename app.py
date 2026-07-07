import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LeetCode Analytics Dashboard",
    layout="wide"
)

st.title("📊 LeetCode Analytics Dashboard")
st.write("Track your coding journey.")

df = pd.read_csv("data/problems.csv")

st.subheader("Solved Problems")
st.dataframe(df)


# Statistics
total = len(df)

easy = len(df[df["Difficulty"] == "Easy"])
medium = len(df[df["Difficulty"] == "Medium"])
hard = len(df[df["Difficulty"] == "Hard"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total", total)
col2.metric("Easy", easy)
col3.metric("Medium", medium)
col4.metric("Hard", hard)

# Difficulty Distribution Chart
difficulty_counts = df["Difficulty"].value_counts()

st.subheader("Difficulty Distribution")

st.bar_chart(difficulty_counts)
topic_counts = df["Topic"].value_counts()

st.subheader("Topic Analysis")

st.bar_chart(topic_counts)