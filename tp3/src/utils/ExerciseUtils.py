import pandas as pd
import numpy as np


class ExerciseUtils:
    """Loads exercise files"""

    def __init__(self):
        raise NotImplementedError("Cannot instantiate class")

    @staticmethod
    def load_ex3_file(path) -> list[int]:
        """Loads exercise 3 file ``TP3-ej3-digitos.txt``"""
        df = pd.read_csv(path, delimiter=' ', header=None)

        # Delete last column bc it contains null values
        df = df.iloc[:, :-1]
        # Get 7x5 matrices and flatten them
        matrix_list = [df.iloc[i:i + 7, :] for i in range(0, len(df), 7)]
        flattened_matrices = [matrix.values.flatten() for matrix in matrix_list]

        return flattened_matrices

    @staticmethod
    def load_ex2_file(path) -> tuple[np.ndarray, np.ndarray]:
        """Loads exercise 2 file ``TP3-ej2-conjunto.csv``"""
        df = pd.read_csv(path)

        inputs = df[['x1', 'x2', 'x3']].to_numpy()
        expected = df['y'].to_numpy()

        return inputs, expected
