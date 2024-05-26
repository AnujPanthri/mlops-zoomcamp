from typing import List, Tuple, Union
import pandas as pd

def split_on_value(
    df: pd.DataFrame,
    feature: str,
    value: Union[int,float,str],
    drop_feature:bool = True,
    return_indexes:bool = False,
) -> Union[Tuple[pd.DataFrame,pd.DataFrame],Tuple[pd.Index,pd.Index]]:

    df_train = df[df[feature] < value]
    df_val = df[df[feature] >= value]

    if return_indexes:
        return df_train.index, df_val.index

    if drop_feature:
        df_train = df_train.drop(columns=[feature])
        df_val = df_val.drop(columns=[feature])

    return df_train, df_val

