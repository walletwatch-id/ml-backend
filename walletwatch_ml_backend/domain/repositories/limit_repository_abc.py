from abc import ABC, abstractmethod
from walletwatch_ml_backend.domain.entities.limit_features import LimitFeatures


class LimitRepositoryABC(ABC):
    """
    Abstract base personality repository
    """

    @abstractmethod
    def predict(self, features: LimitFeatures) -> int:
        """
        Predict limit based on the given features.

        Args:
          features (LimitFeatures): Features object containing the features to be predicted for.

        Returns:
          int: Predicted limit.
        """
        raise NotImplementedError
