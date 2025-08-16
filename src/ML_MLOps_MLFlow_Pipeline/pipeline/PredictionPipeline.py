import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self) -> None:
        self.model = joblib.load(
            "E:/ProjectPractice/E2E-ML-Pipeline-MLOps-MLFlow/artifacts/model_trainer/model.joblib"
        )

    def predict(self, data):
        return self.model.predict(data)
