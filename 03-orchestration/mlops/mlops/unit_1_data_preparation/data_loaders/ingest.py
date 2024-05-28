from typing import List
import pandas as pd


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs) -> pd.DataFrame:
    """
    used for downloading nyc taxi dataset

    Returns:
        df: pd.Dataframe = dataframe containing nyc taxi dataset
    """
    dfs:List[pd.DataFrame] = []

    for year,months in [(2024,(1,2))]:
        for month in months:

            dataset_url = (
                "https://d37ci6vzurychx.cloudfront.net/trip-data/"
                "green_tripdata_{}-{:02}.parquet".format(year,month)
                )
            
            df = pd.read_parquet(dataset_url)
            dfs.append(df)

    return pd.concat(dfs)