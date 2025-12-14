import streamlit as st
import itertools
import pandas as pd

st.set_page_config(page_title="Daily Task Optimizer", page_icon="🧠", layout="wide")

st.title("🧠 Daily Task Optimizer")
st.write("Optimize your day by choosing the most valuable tasks within your available time.")


# ----------------------------------------------------------------------------
# Helper function: solve knapsack (brute force)
# ----------------------------------------------------------------------------
def optimize_tasks(tasks, available_time):
    best_value = 0
    best_combo = []

    for r in range(1, len(tasks) + 1):
        for combo in itertools.combinations(tasks, r):
            total_time = sum(t["time"] for t in combo)
            total_value = sum(t["importance"] for t in combo)

            if total_time <= available_time and total_value > best_value:
                best_value = total_value
                best_combo = combo

    return best_combo, best_value


# ----------------------------------------------------------------------------
# Inputs
# ----------------------------------------------------------------------------
st.subheader("Step 1: Enter Your Available Time")
available_time = st.number_input(
    "How many hours do you have today?",
    min_value=1.0,
    max_value=24.0,
    value=8.0
)

st.subheader("Step 2: Add Your Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3, col4 = st.columns(4)

with col1:
    task_name = st.text_input("Task name")

with col2:
    task_time = st.number_input("Hours required", min_value=0.25, max_value=12.0, step=0.25)

with col3:
    task_importance = st.slider("Importance (1–5)", 1, 5, 3)

with col4:
    category = st.selectbox("Category", ["Work", "School", "Personal", "Health", "Other"])

if st.button("Add Task"):
    if task_name:
        st.session_state.tasks.append({
            "name": task_name,
            "time": task_time,
            "importance": task_importance,
            "category": category
        })
        st.success(f"Added task: {task_name}")
    else:
        st.error("Please enter a task name.")


# ----------------------------------------------------------------------------
# Display tasks
# ----------------------------------------------------------------------------
if st.session_state.tasks:
    st.subheader("Your Tasks")

    df_tasks = pd.DataFrame(st.session_state.tasks)
    st.dataframe(df_tasks)

    # ----------------------------------------------------------------------------
    # Optimization
    # ----------------------------------------------------------------------------
    st.subheader("Step 3: Optimize Your Day")

    if st.button("Run Optimizer"):
        best_combo, best_value = optimize_tasks(st.session_state.tasks, available_time)

        st.success("✨ Optimized Schedule Generated!")

        total_time = sum(t["time"] for t in best_combo)

        st.write(f"**Total Time:** {total_time:.2f} / {available_time} hours")
        st.write(f"**Total Productivity Score:** {best_value}")

        # Display chosen tasks
        st.write("### ✔️ Recommended Tasks")
        for t in best_combo:
            st.write(f"- **{t['name']}** — {t['time']} hrs — importance {t['importance']} — *{t['category']}*")

        # Display postponed tasks
        st.write("### ⏸️ Postponed Tasks")
        postponed = [t for t in st.session_state.tasks if t not in best_combo]
        if postponed:
            for t in postponed:
                st.write(f"- {t['name']}")
        else:
            st.write("You are completing all tasks today!")

        # ----------------------------------------------------------------------------
        # A. TIMELINE CHART (GANTT STYLE)
        # ----------------------------------------------------------------------------
        st.subheader("📊 Timeline Schedule")

        start_time = 0
        schedule = []
        for t in best_combo:
            schedule.append({
                "Task": t["name"],
                "Start": start_time,
                "End": start_time + t["time"]
            })
            start_time += t["time"]

        if schedule:
            df_schedule = pd.DataFrame(schedule)
            st.bar_chart(df_schedule.set_index("Task")[["Start", "End"]])

        # ----------------------------------------------------------------------------
        # B. WHAT-IF SCENARIOS
        # ----------------------------------------------------------------------------
        st.subheader("🔍 What-If Analysis")

        for delta in [-1, +1, +2]:
            new_time = max(1, available_time + delta)
            combo, val = optimize_tasks(st.session_state.tasks, new_time)
            st.write(f"**If you had {new_time} hours:** Best score = {val} (Tasks: {len(combo)})")
