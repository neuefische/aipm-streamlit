# ML → API → Streamlit Demo

This folder contains a small end-to-end exercise: train a simple iris classifier, expose it via FastAPI, and query it from a Streamlit UI.

## Files
- [train_model.py](train_model.py) — trains a LogisticRegression on the iris dataset and saves `artifacts/iris_model.joblib`. (Redundant with the notebook; keep whichever you prefer for automation vs. teaching.)
- [04_train_and_save_model.ipynb](04_train_and_save_model.ipynb) — notebook version of the same training flow.
- [model_api.py](model_api.py) — FastAPI service with `/predict` that loads the saved model.
- [streamlit_api_client.py](streamlit_api_client.py) — Streamlit client to send feature inputs to the API and view predictions.
- [artifacts/](artifacts/) — model and label files produced by training.

## Prerequisites
From the repo root (`aipm-streamlit`):
1) Create/activate a venv (if not already):
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
   - Windows: `python -m venv .venv && .venv\\Scripts\\Activate.ps1`
2) Install deps: `pip install -r requirements.txt`

## Steps
1) Train the model
   - Script: `python ml_api_demo/train_model.py`
   - Notebook: open `ml_api_demo/04_train_and_save_model.ipynb` and run all cells
   - Output: `ml_api_demo/artifacts/iris_model.joblib`

2) Start the API (after training)
   - `uvicorn ml_api_demo.model_api:app --reload --port 8001`
   - Smoke test:
     ```bash
     curl -X POST http://127.0.0.1:8001/predict \
       -H "Content-Type: application/json" \
       -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
     ```

3) Run the Streamlit client
   - `streamlit run ml_api_demo/streamlit_api_client.py`
   - Keep the API running on `http://127.0.0.1:8001` or update the base URL in the UI.

## Notes
- The model uses the built-in iris dataset; swap in your data by editing `train_model.py` and retraining.
- The API expects four float features: sepal_length, sepal_width, petal_length, petal_width.
- If `uvicorn` cannot import `ml_api_demo.model_api`, ensure you run the command from the repo root so Python finds the package.
- Regenerate the model any time you change training code: rerun step 1, then restart the API.
