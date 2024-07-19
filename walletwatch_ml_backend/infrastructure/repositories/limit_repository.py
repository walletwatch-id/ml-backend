from numpy import array, float32, int64
from onnxruntime import InferenceSession
from os import path
from walletwatch_ml_backend.domain.entities.limit_features import LimitFeatures
from walletwatch_ml_backend.domain.repositories.limit_repository_abc import LimitRepositoryABC


class LimitRepository(LimitRepositoryABC):
    session: InferenceSession

    def __init__(self):
        current_dir = path.dirname(path.abspath(__file__))

        with open(f'{current_dir}/../resources/limit.onnx', 'rb') as f:
            model = f.read()

        self.session = InferenceSession(
            model, providers=['CPUExecutionProvider']
        )

    def predict(self, features: LimitFeatures) -> int:
        features = {
            'total_incomes': array([features.total_incomes]).reshape(-1, 1).astype(int64),
            'total_transactions': array([features.total_transactions]).reshape(-1, 1).astype(int64),
            'personality': array([features.personality]).reshape(-1, 1),
            'last_month_limit': array([features.last_month_limit]).reshape(-1, 1).astype(float32)
        }

        prediction = self.session.run(None, features)

        result = prediction[0][0][0].tolist()

        return result
