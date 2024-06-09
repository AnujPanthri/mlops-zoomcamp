import pickle
import pandas as pd
import numpy as np
import sys


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


def main(month,year):
    
    output_file = "batch_preds.parquet"
    print(month,year)
    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    print("standard deviation of predictions:",y_pred.std())
    print("mean of predictions:",y_pred.mean())

    df_results = pd.DataFrame()
    df_results['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    df_results['predictions'] = y_pred

    df_results.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

if __name__=="__main__":
    if (len(sys.argv)==1):
        print("you need to pass month and year as positional args")
        exit()
    elif(len(sys.argv)==2):
        print("you also need to pass the year as positional arg")
        exit()
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    main(month,year)