

from walletwatch_ml_backend.domain.entities.limit_features import LimitFeatures
from walletwatch_ml_backend.domain.entities.personality_features import PersonalityFeatures
from walletwatch_ml_backend.domain.repositories.limit_repository_abc import LimitRepositoryABC
from walletwatch_ml_backend.domain.repositories.personality_repository_abc import PersonalityRepositoryABC


class Predict:
    limit_repository: LimitRepositoryABC
    personality_repository: PersonalityRepositoryABC

    def __init__(self, limit_repository: LimitRepositoryABC, personality_repository: PersonalityRepositoryABC):
        self.limit_repository = limit_repository
        self.personality_repository = personality_repository

    def __call__(self, model_id: str, features: LimitFeatures | PersonalityFeatures) -> int | str:
        match model_id:
            case 'limit':
                return self.limit_repository.predict(features)
            case 'personality':
                return self.personality_repository.predict(features)
            case _:
                raise ValueError(f'Invalid model ID: {model_id}')
