import numpy as np

from src.classes.similarity.SimilarityABC import SimilarityABC


class Euclidean(SimilarityABC):
    """
    Calculates similirity using the follwoing formula: ||Xp - Wj||
    """

    @classmethod
    def calculate(cls, expected: float, weights: list[float]) -> float:
        return np.linalg.norm(np.array(expected)-np.array(weights), 2)
