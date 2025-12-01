"""
Streamlit Widgets and Session State lab.

Run this file with:
    streamlit run 02_streamlit_widgets_state.py

What to explore:
- Keeping values across reruns with `st.session_state`.
- Using buttons and callbacks to mutate state.
- Grouping inputs with forms.
"""
import streamlit as st

st.set_page_config(page_title="Streamlit Widgets and State", layout="centered")  # Basic page setup

st.title("Counter demo")

if "count" not in st.session_state:
    st.session_state.count = 0  # Initialize state only once per browser session

st.write(f"Current count: {st.session_state.count}")

if st.button("Increment"):
    st.session_state.count += 1  # Button triggers a rerun; state persists

if st.button("Reset"):
    st.session_state.count = 0  # Another button shares the same state store

st.caption("State lives across reruns. Combine it with text inputs and selects.")

st.divider()
st.subheader("Profile form")

with st.form("profile"):
    name = st.text_input("Name")  # Widgets inside a form defer updates
    role = st.selectbox("Role", ["Engineer", "Designer", "PM"])
    subscribed = st.checkbox("Subscribe to updates")
    submitted = st.form_submit_button("Save")  # Submission triggers a single rerun

if submitted:
    st.success(f"Saved {name or 'anonymous'} ({role}) | subscribed={subscribed}")  # Form values available after submit

st.markdown(
    """
Stretch goals:
- Add validation (require a name before saving).
- Add a callback that increments a "saves" counter in `st.session_state`.
- Log the state dictionary with `st.write(st.session_state)` to see what Streamlit tracks.
    """
)
