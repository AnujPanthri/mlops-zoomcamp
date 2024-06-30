import os
import pandas as pd
from datetime import datetime
import pandas as pd
import dotenv

dotenv.load_dotenv()

os.environ["INPUT_FILE_PATTERN"] = "s3://nyc-duration/{month:02d}_{year:04d}.parquet"
os.environ["OUTPUT_FILE_PATTERN"] = "s3://nyc-duration/test_prediction_{month:02d}_{year:04d}.parquet"

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
]

columns = ["PULocationID", "DOLocationID", "tpep_pickup_datetime", "tpep_dropoff_datetime"]
df_input = pd.DataFrame(data, columns=columns)
year = 2023
month = 1 
input_file = os.environ["INPUT_FILE_PATTERN"].format(year=year, month=month)

S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")

options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL,
    },
}

df_input.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)
os.environ["S3_ENDPOINT_URL"] = "http://localhost:4566"

os.system(f"cd .. && python batch.py --month {month} --year {year}")
prediction_df = pd.read_parquet(os.environ["OUTPUT_FILE_PATTERN"].format(year=year, month=month))

prediction_sum = prediction_df.predicted_duration.sum()
print("sum of predictions:", prediction_sum)

expected_sum = 36.28

assert abs(prediction_sum-expected_sum)<1e-2