"""
Minimal Streamlit task board demo used in the notebooks.

Quickstart:
    streamlit run main.py
    # then open the local URL in your browser
"""
from __future__ import annotations

from typing import Dict, List

import streamlit as st

# Sample data used to seed the in-memory task list
def _seed_tasks() -> List[Dict[str, object]]:
    return [
        {
            "id": 1,
            "title": "Review Streamlit docs",
            "description": "Skim the Streamlit docs to understand layout, widgets, and reruns.",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Build first widget",
            "description": "Render text, inputs, and a chart in a single page app.",
            "completed": True,
        },
        {
            "id": 3,
            "title": "Ship a task board",
            "description": "Use session state to add, toggle, and delete tasks on the fly.",
            "completed": False,
        },
    ]


def init_state() -> None:
    """Ensure session_state has a task list and next ID."""
    if "tasks" not in st.session_state:
        st.session_state.tasks = _seed_tasks()
        st.session_state.next_id = len(st.session_state.tasks) + 1


# ---- mutations ----

def add_task(title: str, description: str, completed: bool = False) -> None:
    st.session_state.tasks.append(
        {
            "id": st.session_state.next_id,
            "title": title,
            "description": description,
            "completed": completed,
        }
    )
    st.session_state.next_id += 1


def toggle_task(task_id: int, completed: bool) -> None:
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            task["completed"] = completed
            return


def delete_task(task_id: int) -> None:
    st.session_state.tasks = [task for task in st.session_state.tasks if task["id"] != task_id]


def reset_tasks() -> None:
    st.session_state.tasks = _seed_tasks()
    st.session_state.next_id = len(st.session_state.tasks) + 1


# ---- helpers ----

def filter_tasks(keyword: str, status: str) -> List[Dict[str, object]]:
    filtered = st.session_state.tasks
    if keyword:
        lowered = keyword.lower()
        filtered = [task for task in filtered if lowered in task["title"].lower()]
    if status == "Completed":
        filtered = [task for task in filtered if task["completed"]]
    elif status == "Open":
        filtered = [task for task in filtered if not task["completed"]]
    return filtered


def main() -> None:
    st.set_page_config(page_title="Streamlit Task Board", page_icon="[]", layout="wide")  # Wide layout for cards/metrics
    init_state()

    st.title("Streamlit Task Board")
    st.caption("Add tasks, filter them, and toggle completion in-memory using session state.")  # State is per browser session

    # Sidebar controls
    with st.sidebar:
        st.header("Filters")
        keyword = st.text_input("Search title", placeholder="e.g. Streamlit")  # Text filter
        status_filter = st.selectbox("Status", ["All", "Open", "Completed"], index=0)
        st.button("Reset sample data", on_click=reset_tasks, type="secondary")  # Re-seed demo data
        st.divider()
        st.markdown(
            "Use this sidebar to narrow the task list. The data lives only in your browser session."
        )

    # Summary metrics
    total_tasks = len(st.session_state.tasks)
    completed_tasks = sum(task["completed"] for task in st.session_state.tasks)
    open_tasks = total_tasks - completed_tasks  # Simple rollups for metrics
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Total tasks", total_tasks)
    col_b.metric("Open", open_tasks)
    col_c.metric("Completed", completed_tasks)

    st.subheader("Create a task")
    with st.form("add-task", clear_on_submit=True):
        title = st.text_input("Title", placeholder="Write a short, actionable title")
        description = st.text_area("Description", placeholder="Optional context or notes", height=80)
        completed = st.checkbox("Mark as completed", value=False)
        submitted = st.form_submit_button("Add task", type="primary")  # Form batches inputs until submit
        if submitted:
            if not title.strip():
                st.warning("Title is required.")
            else:
                add_task(title.strip(), description.strip(), completed)
                st.success("Task added to the board.")

    st.divider()
    st.subheader("Tasks")

    filtered_tasks = filter_tasks(keyword=keyword, status=status_filter)  # Apply sidebar filters

    if not filtered_tasks:
        st.info("No tasks match the current filters. Add one above or clear the filters.")
        return

    for task in filtered_tasks:
        expander_label = f"{task['title']} (#{task['id']})"
        with st.expander(expander_label, expanded=False):
            st.write(task["description"] or "No description")
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                new_status = st.checkbox(
                    "Completed", value=bool(task["completed"]), key=f"completed-{task['id']}"
                )  # Each checkbox needs a stable key to persist across reruns
                if new_status != task["completed"]:
                    toggle_task(task_id=task["id"], completed=new_status)
            with col2:
                st.write(f"Status: {'Done' if task['completed'] else 'Open'}")  # Quick label
            with col3:
                st.button(
                    "Delete task",
                    key=f"delete-{task['id']}",
                    on_click=delete_task,
                    args=(task["id"],),
                    type="secondary",
                )  # Deletes the task from session state


if __name__ == "__main__":
    main()
