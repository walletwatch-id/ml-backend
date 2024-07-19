from numpy import load
from onnxruntime import InferenceSession
from os import path
from pandas import DataFrame
from sklearn.calibration import LabelEncoder
from walletwatch_ml_backend.domain.entities.personality_features import PersonalityFeatures
from walletwatch_ml_backend.domain.repositories.personality_repository_abc import PersonalityRepositoryABC


class PersonalityRepository(PersonalityRepositoryABC):
    encoder: LabelEncoder
    session: InferenceSession

    def __init__(self):
        current_dir = path.dirname(path.abspath(__file__))

        with open(f'{current_dir}/../resources/personality.onnx', 'rb') as f:
            model = f.read()

        self.session = InferenceSession(
            model, providers=['CPUExecutionProvider'])
        self.encoder = LabelEncoder()
        self.encoder.classes_ = load(
            f'{current_dir}/../resources/personality-encoder.npy',
            allow_pickle=True,
        )

    def predict(self, features: PersonalityFeatures) -> str:
        features = DataFrame([vars(features)])

        prediction = self.session.run(None, {'X': features.values})[0]

        result = self.encoder.inverse_transform(prediction)[0]

        return result
