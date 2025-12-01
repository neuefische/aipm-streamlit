# Streamlit Fundamentals learning repo

This repo provides three Python lab scripts for Streamlit basics, a task-board demo, and an end-to-end ML → API → Streamlit exercise kept in `ml_api_demo/`.

## Files
- `01_streamlit_fundamentals.py` — Text, inputs, layout, and reruns.
- `02_streamlit_widgets_state.py` — Forms, session state, callbacks, and reusable helper functions.
- `03_streamlit_data_app.py` — Filtering, tables, charts, and UX polish.
- `ml_api_demo/04_train_and_save_model.ipynb` / `ml_api_demo/train_model.py` — Train and save an iris classifier to `ml_api_demo/artifacts/iris_model.joblib`.
- `ml_api_demo/model_api.py` — FastAPI service exposing `/predict` from the saved model.
- `ml_api_demo/streamlit_api_client.py` — Streamlit UI to call the API.
- `main.py` — Task-board demo that combines UI patterns.
- `INSTRUCTIONS.md` — Setup steps, run commands, and learning path.

## How to use
1. Create a virtual environment and install deps: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
2. Run the UI labs with `streamlit run <file>` in order (see `INSTRUCTIONS.md`).
3. Train the model (notebook or script), start the API, then query it via `ml_api_demo/streamlit_api_client.py`.
4. Launch `streamlit run main.py` to see the combined task-board app.

## Suggested learning path
- Start with Streamlit Fundamentals to learn the rendering model.
- Move to Widgets + State to capture user input reliably.
- Finish with Data App to combine layout, data display, and structure.
- Do the ML → API → Streamlit flow to practice backend/frontend integration.
