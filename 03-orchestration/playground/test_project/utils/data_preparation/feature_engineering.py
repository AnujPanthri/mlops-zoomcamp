import pandas as pd
from typing import Dict,List,Union

def combine_features(
    df: Union[List[Dict], pd.DataFrame]
    ) ->Union[List[Dict], pd.DataFrame]:
    
    if isinstance(df,pd.DataFrame):
        # pickup and dropoff
        df["PU_DO"] = df["PULocationID"] + "_" + df["DOLocationID"]
    
    elif isinstance(df,list) and len(df) >=1 and isinstance(df[0],dict):
        arr = []
        for row in df:
            row["PU_DO"] = str(row["PULocationID"]) + "_" + str(row["DOLocationID"])
            arr.append(row)
        return arr

    return df