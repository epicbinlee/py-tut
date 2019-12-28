import pandas as pd


class DfHelper:

    @staticmethod
    def read_csv(path: str, col_names: list):
        df: pd.DataFrame = pd.read_csv(path, names=col_names)
        return df.shape
