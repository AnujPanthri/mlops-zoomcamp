import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data(
    *args,
    **kwargs,
) -> pd.DataFrame:
    """
    loads March 2023 yellow taxi trips dataset
    """
    
    df = pd.read_parquet(
        "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
    )

    return df