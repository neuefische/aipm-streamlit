"""
Streamlit Data App lab.

Run this file with:
    streamlit run 03_streamlit_data_app.py

What to explore:
- Combining data, filters, and layout to build a small dashboard.
- Using multiselects and charts.
- Applying the same pattern to your own CSV or API data.
"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Streamlit Data App", layout="wide")  # Wider layout for tables/charts

st.title("Mini sales dashboard")

data = pd.DataFrame(
    {
        "region": ["North", "South", "West", "East"],
        "sales": [120, 95, 140, 110],
        "rep": ["Alex", "Blake", "Casey", "Dakota"],
    }
)

region_filter = st.multiselect(
    "Regions", options=sorted(data["region"].unique()), default=list(data["region"].unique())
)  # Multiselect drives the filtered view
filtered = data[data["region"].isin(region_filter)]  # Simple filter using the selection

st.subheader("Table")
st.dataframe(filtered, use_container_width=True)  # Show current slice of data

st.subheader("Chart")
st.bar_chart(filtered, x="region", y="sales")  # Visualize sales per region for the filtered set

st.markdown(
    """
Next steps:
- Add a search box for reps (`st.text_input`) and filter the table.
- Add date filters if you load time series data.
- Show summary metrics with `st.metric` or `st.columns`.
    """
)
