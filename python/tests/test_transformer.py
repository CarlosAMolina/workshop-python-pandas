import pathlib
import pickle
import sys
import unittest

import pandas as pd

sys.path.append(f"{pathlib.Path().absolute()}/etl")

from etl.transformer import Transformer


class TestTransformer(unittest.TestCase):

    def setUp(self):
        with open("tests/files/pickle/dfs_from_db", "rb") as f:
            self.dfs = pickle.load(f)

    def test_result_without_duplicated_primary_keys(self):
        primary_keys = ["id", "year"]
        result_df = Transformer.get_df(self.dfs)
        result_df_without_duplicated_primary_keys = result_df.drop_duplicates(
            subset=primary_keys
        )
        self.assertEqual(len(result_df), len(result_df_without_duplicated_primary_keys))

