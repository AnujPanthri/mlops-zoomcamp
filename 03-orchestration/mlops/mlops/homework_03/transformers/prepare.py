if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(
    df,
    *args,
    **kwargs,
) -> None:
    """
    prepare the dataset
    """

    # duration in minutes
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df.duration = df.duration.apply(lambda x: x.total_seconds()/60)

    # removing outliers
    df = df[(df.duration>=1) & (df.duration<=60)]

    categorical = [ 'PULocationID', 'DOLocationID' ]
    df[categorical] = df[categorical].astype(str)

    return df
