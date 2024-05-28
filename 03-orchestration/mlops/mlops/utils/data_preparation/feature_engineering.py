from typing import Union,List,Dict
from pandas import DataFrame


def combine_features(
    df: Union[DataFrame, List[Dict]],
) -> Union[DataFrame, List[Dict]]:
    
    if isinstance(df, DataFrame):
        df["PU_DO"] = df["PULocationID"] + "_" + df["DOLocationID"]
    
    elif isinstance(df, List) and len(df)>=1 and isinstance(df[0], Dict):
        arr = []
        for row in df:
            row["PU_DO"] = str(row["PULocationID"]) + "_" + str(row["DOLocationID"])
            arr.append(row)
        return arr

    return df