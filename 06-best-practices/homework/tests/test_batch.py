import batch
from datetime import datetime
import pandas as pd

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

def test_demo():
    assert 1==1

def test_read_data():
    
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]

    columns = ["PULocationID", "DOLocationID", "tpep_pickup_datetime", "tpep_dropoff_datetime"]
    df = pd.DataFrame(data, columns=columns)
    categorical = ['PULocationID', 'DOLocationID']

    actual_df = batch.prepare_data(df, categorical)
    # actual_result = 
    expected_result = [
        ("-1", "-1", dt(1, 1), dt(1, 10), 9),
        ("1", "1", dt(1, 2), dt(1, 10), 8),
    ]
    expected_columns = ["PULocationID", "DOLocationID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "duration"]
    expected_df = pd.DataFrame(expected_result, columns=expected_columns)

    actual_records = actual_df.to_dict(orient="records")
    expected_records = expected_df.to_dict(orient="records")
    
    assert len(actual_records)==len(expected_records)

    for i in range(len(expected_records)):
        assert actual_records[i]==expected_records[i]