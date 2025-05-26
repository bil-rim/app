import streamlit as st
import datetime

# Title
st.title("📋 To-Do List — Daily Activity Tracker")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input section
with st.form("add_task_form", clear_on_submit=True):
    task = st.text_input("Add a new task")
    submitted = st.form_submit_button("➕ Add Task")
    if submitted and task:
        st.session_state.tasks.append({"task": task, "done": False})

# Display today's date
st.write(f"🗓️ **Today:** {datetime.date.today().strftime('%A, %d %B %Y')}")

# Show tasks
st.subheader("📌 Tasks for Today")

for i, t in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
    with col1:
        st.write(f"✅ {t['task']}" if t["done"] else f"🔲 {t['task']}")
    with col2:
        if st.button("Mark Done", key=f"done_{i}"):
            st.session_state.tasks[i]["done"] = True
    with col3:
        if st.button("❌ Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
