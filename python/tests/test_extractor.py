from unittest import mock
import unittest

import pandas as pd

from etl.extractor import Extractor


class TestExtractor(unittest.TestCase):

    @mock.patch("etl.extractor.Extractor._get_db_table_as_df")
    @mock.patch("etl.extractor.Extractor._get_db_engine")
    def test_get_db_data_returns_correct_type(
        self,
        mock_get_db_engine,
        mock_get_db_table_as_df,
    ):
        mock_get_db_engine.return_value = mock.MagicMock()
        mock_get_db_table_as_df.return_value = pd.DataFrame(data={})
        dfs = Extractor.get_dfs()
        self.assertEqual(len(dfs), 2)
        self.assertTrue(all(isinstance(df, pd.DataFrame) for df in dfs))
