"""
Train and save a simple iris classifier.

Run from repo root:
    python ml_api_demo/train_model.py

This writes ml_api_demo/artifacts/iris_model.joblib and prints accuracy.
"""
from __future__ import annotations

from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def train_and_save() -> None:
    data = load_iris()
    X = data["data"]
    y = data["target"]
    target_names = data["target_names"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.3f}")
    print(classification_report(y_test, y_pred, target_names=target_names))

    artifacts = Path(__file__).parent / "artifacts"
    artifacts.mkdir(exist_ok=True)
    model_path = artifacts / "iris_model.joblib"

    joblib.dump(
        {
            "model": model,
            "feature_names": data["feature_names"],
            "target_names": target_names,
        },
        model_path,
    )
    print(f"Saved model to {model_path}")


def main() -> None:
    train_and_save()


if __name__ == "__main__":
    main()
