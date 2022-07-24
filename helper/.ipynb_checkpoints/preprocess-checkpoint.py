import pandas as pd
import numpy as np
from sklearn import preprocessing


def standard_scaler(df: pd.DataFrame):
    """Scaling standard scaler transform."""
    index_cols = df.index
    scaler = preprocessing.StandardScaler()
    np_scaler = scaler.fit_transform(df)
    df_transformed = pd.DataFrame(
        np_scaler, index=index_cols, columns=df.columns
    )
    return scaler, df_transformed