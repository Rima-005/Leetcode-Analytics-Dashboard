import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LeetCode Analytics Dashboard",
    layout="wide"
)

st.title("📊 LeetCode Analytics Dashboard")
st.write("Track your coding journey.")

df = pd.read_csv("data/problems.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.subheader("Solved Problems")

search = st.text_input("🔍 Search Problems")

filtered_df = df[
    df["Problem"].str.contains(
        search,
        case=False,
        na=False
    )
]

st.dataframe(filtered_df)

unique_dates = sorted(df["Date"].dt.date.unique())

streak = 0

if len(unique_dates) > 0:

    streak = 1

    for i in range(len(unique_dates)-1, 0, -1):

        diff = (unique_dates[i] - unique_dates[i-1]).days

        if diff == 1:
            streak += 1
        else:
            break

st.metric(" Current Streak", streak)

goal = 300

progress = len(df)

percentage = min(progress / goal, 1.0)

st.subheader("Goal Progress")

st.progress(percentage)

st.write(f"{progress}/{goal} Problems Solved")

st.subheader(" Monthly Progress")

monthly_progress = (
    df.groupby(df["Date"].dt.to_period("M"))
    .size()
)

monthly_progress.index = monthly_progress.index.astype(str)

st.line_chart(monthly_progress)


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
st.subheader("Add New Problem")

with st.form("problem_form"):

    problem_name = st.text_input("Problem Name")

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    topic = st.text_input("Topic")

    date = st.date_input("Date Solved")

    submit = st.form_submit_button("Add Problem")

if submit:

    new_problem = pd.DataFrame({
        "Problem": [problem_name],
        "Difficulty": [difficulty],
        "Topic": [topic],
        "Date": [date]
    })

    df = pd.concat([df, new_problem], ignore_index=True)

    df.to_csv("data/problems.csv", index=False)

    st.success("Problem added successfully!")