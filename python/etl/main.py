from extractor import Extractor
from transformer import Transformer


if __name__ == "__main__":
    dfs = Extractor.get_dfs()
    df = Transformer.get_df(dfs)
    print(df)
