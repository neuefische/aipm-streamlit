# Streamlit Fundamentals and Data App Labs

Practice Streamlit basics and build a small interactive task board in three short Python lab scripts (no notebooks), plus an end-to-end ML → API → Streamlit exercise.

## Environment setup
1) Python 3.11 recommended (optional): `pyenv local 3.11.3`
2) Create/activate a virtual environment:
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `python -m venv .venv && .venv\\Scripts\\Activate.ps1`
3) Install deps: `pip install --upgrade pip && pip install -r requirements.txt`

## Contents (suggested order)
1. [01_streamlit_fundamentals.py](01_streamlit_fundamentals.py) — First steps with Streamlit, page layout, text, inputs, and reruns.
2. [02_streamlit_widgets_state.py](02_streamlit_widgets_state.py) — Forms, session state, callbacks, and handling user input.
3. [03_streamlit_data_app.py](03_streamlit_data_app.py) — Building a simple data app with tables, filtering, and tidy UI patterns.
4. [main.py](main.py) — Task-board app that combines the lab patterns (add/filter/complete/delete tasks).
5. [ml_api_demo/](ml_api_demo/) — Self-contained ML → API → Streamlit exercise (notebook + redundant script for headless retraining):
   - [04_train_and_save_model.ipynb](ml_api_demo/04_train_and_save_model.ipynb) — Train and save a simple iris classifier (produces `ml_api_demo/artifacts/iris_model.joblib`).
   - [train_model.py](ml_api_demo/train_model.py) — Script alternative to produce the same artifact without notebooks.
   - [model_api.py](ml_api_demo/model_api.py) — FastAPI service that loads the saved model and exposes `/predict`.
   - [streamlit_api_client.py](ml_api_demo/streamlit_api_client.py) — Streamlit UI to call the API and view predictions.
   - More detail: see [ml_api_demo/README.md](ml_api_demo/README.md).

## Run the Streamlit labs (UI patterns)
- Fundamentals: `streamlit run 01_streamlit_fundamentals.py`
- Widgets + State: `streamlit run 02_streamlit_widgets_state.py`
- Data App: `streamlit run 03_streamlit_data_app.py`
- Task board demo: `streamlit run main.py`

## End-to-end ML → API → Streamlit (in `ml_api_demo/`)
1) Train and save the model
   - Notebook: run `ml_api_demo/04_train_and_save_model.ipynb`
   - Script: `python ml_api_demo/train_model.py`
   - Output: `ml_api_demo/artifacts/iris_model.joblib`
2) Start the API
   - `uvicorn ml_api_demo.model_api:app --reload --port 8001`
   - Test:
     ```bash
     curl -X POST http://127.0.0.1:8001/predict \
       -H "Content-Type: application/json" \
       -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
     ```
3) Query from Streamlit
   - `streamlit run ml_api_demo/streamlit_api_client.py`
   - Point the client at `http://127.0.0.1:8001` and send predictions.
