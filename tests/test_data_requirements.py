from unittest import TestCase


class TestDataImports(TestCase):
    def test_matplotlib(self):
        import matplotlib.pyplot as plt

        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    
    def test_numpy(self):
        import numpy as np

        shape = (2, 3)

        sum_ones = np.ones(shape, dtype=np.int16).sum()

        self.assertEqual(sum_ones, shape[0] * shape[1])
    
    def test_pandas(self):
        import pandas as pd

        length = 100

        df = pd.DataFrame(
            {
                "A": [1] * length
            }
        )

        self.assertEqual(sum(df["A"]), length)
