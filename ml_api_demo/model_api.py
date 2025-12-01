"""
FastAPI service that loads the saved iris model and exposes a predict endpoint.

Run after training (from repo root):
    uvicorn ml_api_demo.model_api:app --reload --port 8001
"""
from __future__ import annotations

from pathlib import Path
from typing import List

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

ARTIFACT_PATH = Path(__file__).parent / "artifacts" / "iris_model.joblib"


class PredictRequest(BaseModel):
    """Feature vector for a single iris measurement."""

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictResponse(BaseModel):
    predicted_class: str
    probabilities: List[float]
    class_labels: List[str]


app = FastAPI(title="Iris Model API", version="1.0.0")

_model = None
_label_names: List[str] = []


@app.on_event("startup")
def load_model() -> None:
    global _model, _label_names
    if not ARTIFACT_PATH.exists():
        raise RuntimeError(
            "Model artifact missing. Run the training notebook or train_model.py to create artifacts/iris_model.joblib."
        )
    payload = joblib.load(ARTIFACT_PATH)
    _model = payload["model"]
    _label_names = list(payload["target_names"])


@app.get("/")
def root() -> dict:
    return {"status": "ok", "model_loaded": _model is not None}


@app.post("/predict", response_model=PredictResponse)
def predict(body: PredictRequest) -> PredictResponse:
    if _model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    vector = [
        body.sepal_length,
        body.sepal_width,
        body.petal_length,
        body.petal_width,
    ]

    probs = _model.predict_proba([vector])[0]
    pred_idx = int(probs.argmax())
    return PredictResponse(
        predicted_class=_label_names[pred_idx],
        probabilities=list(map(float, probs)),
        class_labels=_label_names,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("model_api:app", host="0.0.0.0", port=8001, reload=True)
