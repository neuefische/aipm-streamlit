"""
Streamlit Fundamentals lab.

Run this file with:
    streamlit run 01_streamlit_fundamentals.py

What to explore:
- How the script reruns on every interaction.
- Basic layout elements (title, subheader, text, chart).
- How widgets capture user input.
"""
import streamlit as st

st.set_page_config(page_title="Streamlit Fundamentals", layout="centered")  # Basic page setup

st.title("Hello Streamlit")
st.subheader("You control layout by top-to-bottom code execution.")

name = st.text_input("Your name", placeholder="Pat")  # Text input reruns the script on change
level = st.slider("Excitement level", min_value=1, max_value=5, value=3)  # Slider also triggers reruns

st.write(f"Hi {name or 'friend'}!")
st.write("You can drag sliders, type text, and the app reruns automatically.")
st.bar_chart([1, 2, 3, 2, level])  # Chart reflects the latest slider state on each rerun

st.markdown(
    """
Try:
- Add another widget (e.g., `st.selectbox`) and print its value.
- Replace `st.bar_chart` with `st.line_chart` or `st.metric`.
- Comment out lines to see how removing a widget changes the UI on rerun.
    """
)
