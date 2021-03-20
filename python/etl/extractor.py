from typing import List

from sqlalchemy import create_engine
import pandas as pd


class Extractor:

    _DB = "funds"
    _PASSWORD = "pw"
    _DB_URL = f"mysql+pymysql://root:{_PASSWORD}@localhost/{_DB}"

    @classmethod
    def get_dfs(cls) -> List[pd.DataFrame]:
        return cls._get_db_tables_as_dfs()

    @classmethod
    def _get_db_tables_as_dfs(cls) -> List[pd.DataFrame]:
        engine = cls._get_db_engine()
        with engine.connect() as connection:
            name_df = cls._get_db_table_as_df("name", connection)
            profitability_df = cls._get_db_table_as_df("profitability", connection)
        return [name_df, profitability_df]

    @classmethod
    def _get_db_engine(cls) -> "sqlalchemy.engine.base.Engine":
        return create_engine(cls._DB_URL)

    @staticmethod
    def _get_db_table_as_df(table_name: str, db_connection) -> pd.DataFrame:
        return pd.read_sql(f"select * from {table_name}", db_connection)
