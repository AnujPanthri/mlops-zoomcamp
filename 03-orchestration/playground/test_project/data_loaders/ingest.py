import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_nyc_taxi_datasets(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    dfs:list[pd.DataFrame] = []
    # Specify your data loading logic here
    for year,months in [(2024,(1,2))]:
        for month in months:
            file_path = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{}-{:02}.parquet".format(year,month)

            df = pd.read_parquet(file_path)
            dfs.append(df)
    return pd.concat(dfs)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert isinstance(output,pd.DataFrame)
