from typing import List

import pandas as pd


class DataFramesExtracted:

    def __init__(self, dfs: List[pd.DataFrame]):
        (
            self.name,
            self.profitability,
        ) = dfs
