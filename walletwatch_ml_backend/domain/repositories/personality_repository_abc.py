from abc import ABC, abstractmethod
from walletwatch_ml_backend.domain.entities.personality_features import PersonalityFeatures


class PersonalityRepositoryABC(ABC):
    """
    Abstract base personality repository
    """

    @abstractmethod
    def predict(self, features: PersonalityFeatures) -> str:
        """
        Predict personality based on the given features.

        Args:
          features (PersonalityFeatures): Features object containing the features to be predicted (f01-f36) with values in likert scale (1-5).

        Returns:
          str: Predicted personality.
        """
        raise NotImplementedError
