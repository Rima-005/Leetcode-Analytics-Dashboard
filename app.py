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