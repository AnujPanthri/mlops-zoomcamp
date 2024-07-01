import pandas as pd

def clean(
    df: pd.DataFrame,
    include_extreme_durations:bool = False
    )-> pd.DataFrame:

    # convert to datetime format
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

    # calculate duration column in minutes
    df['duration'] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
    df.duration = df.duration.apply(lambda x: x.total_seconds()/60)

    # remove outliers
    if (include_extreme_durations):
        valid_idxs = (df.duration>=1) & (df.duration<60)
        df = df[valid_idxs]

    # convert categorical columns to type object
    categorical = ["PULocationID", "DOLocationID"]
    df[categorical] = df[categorical].astype(str)

    return df