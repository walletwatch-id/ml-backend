import runpod
from walletwatch_ml_backend.application.predict import Predict
from walletwatch_ml_backend.domain.entities.limit_features import LimitFeatures
from walletwatch_ml_backend.domain.entities.personality_features import PersonalityFeatures
from walletwatch_ml_backend.domain.repositories.limit_repository_abc import LimitRepositoryABC
from walletwatch_ml_backend.domain.repositories.personality_repository_abc import PersonalityRepositoryABC
from walletwatch_ml_backend.infrastructure.repositories.limit_repository import LimitRepository
from walletwatch_ml_backend.infrastructure.repositories.personality_repository import PersonalityRepository


# Repositories
limit_repository: LimitRepositoryABC = LimitRepository()
personality_repository: PersonalityRepositoryABC = PersonalityRepository()

# Use case
predict = Predict(limit_repository, personality_repository)

def handler(job):
    """ Handler function that will be used to process jobs. """

    job_input = job['input']

    model_id = job_input.get('model_id')
    features = job_input.get('features')

    match model_id:
        case 'limit':
            features = LimitFeatures(**features)
        case 'personality':
            features = PersonalityFeatures(**features)

    return predict(model_id, features)


if __name__ == '__main__':
    runpod.serverless.start({"handler": handler})
