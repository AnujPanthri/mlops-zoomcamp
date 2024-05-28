from typing import Optional
import pandas as pd

def clean(
    df: pd.DataFrame,
    include_extreme_durations: Optional[bool] = False
) -> pd.DataFrame:

    # Convert pick and drop datetime to datatime datatype
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    # Calculate the trip duration & convert to minutes
    df["duration"] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
    df.duration = df.duration.apply(lambda x: x.total_seconds() / 60)

    if not include_extreme_durations:
        df = df[(df.duration>=1) & (df.duration<=60)]
    
    # Convert location IDs to string to treat them as categorical features
    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)

    return df