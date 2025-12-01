"""
Streamlit client to send requests to the iris model API.

Run after the API is up (from repo root):
    streamlit run ml_api_demo/streamlit_api_client.py
"""
from __future__ import annotations

import requests
import streamlit as st

DEFAULT_API_URL = "http://127.0.0.1:8001"

st.set_page_config(page_title="Iris Model Client", layout="centered")  # Keep UI narrow for form
st.title("Query the Iris Model API")
st.caption("Enter measurements, call the FastAPI service, and view the predicted class.")

api_url = st.text_input("API base URL", value=DEFAULT_API_URL)  # Allow overriding host/port

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Sepal length", min_value=0.0, max_value=10.0, value=5.1, step=0.1)
    sepal_width = st.number_input("Sepal width", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
with col2:
    petal_length = st.number_input("Petal length", min_value=0.0, max_value=10.0, value=1.4, step=0.1)
    petal_width = st.number_input("Petal width", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

if st.button("Predict", type="primary"):  # Submit payload to the API
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }
    try:
        resp = requests.post(f"{api_url}/predict", json=payload, timeout=5)  # Call FastAPI
        resp.raise_for_status()
        data = resp.json()
        st.success(f"Predicted: {data['predicted_class']}")  # Show top class
        st.write("Probabilities:")
        for label, prob in zip(data["class_labels"], data["probabilities"]):
            st.write(f"- {label}: {prob:.3f}")  # Display class distribution
    except Exception as exc:  # noqa: BLE001
        st.error(f"Request failed: {exc}")

st.markdown(
    """
How to run:
1) Train the model (notebook `ml_api_demo/04_train_and_save_model.ipynb` or `python ml_api_demo/train_model.py`).
2) Start the API: `uvicorn ml_api_demo.model_api:app --reload --port 8001`.
3) Run this client: `streamlit run ml_api_demo/streamlit_api_client.py`.
    """
)
