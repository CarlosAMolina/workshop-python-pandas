from typing import List

import pandas as pd

from dataframes_extracted import DataFramesExtracted


class Transformer:
    @classmethod
    def get_df(cls, dfs: List[pd.DataFrame]) -> pd.DataFrame:
        dfs = DataFramesExtracted(dfs)
        result_df = cls._merge_dfs(dfs)
        result_df = cls._get_df_remove_null_profitability(result_df)
        result_df = cls._get_df_max_profitability_for_each_fund(result_df)
        result_df = cls._get_df_reindex_columns(result_df)
        return result_df

    @staticmethod
    def _merge_dfs(dfs: DataFramesExtracted) -> pd.DataFrame:
        return dfs.name.merge(
            dfs.profitability,
            on="id",
            how="left",
        )

    @staticmethod
    def _get_df_remove_null_profitability(df: pd.DataFrame) -> pd.DataFrame:
        return df[df.profitability.notnull()]

    @staticmethod
    def _get_df_max_profitability_for_each_fund(df: pd.DataFrame) -> pd.DataFrame:
        result_df = df[["id", "profitability"]]
        result_df = result_df.groupby(["id"], as_index=False).max()
        result_df = result_df.merge(
            df,
            on=["id", "profitability"],
            how="left",
        )
        return result_df

    @staticmethod
    def _get_df_reindex_columns(df: pd.DataFrame) -> pd.DataFrame:
        return df.reindex(columns=["id", "name", "year", "profitability"])
