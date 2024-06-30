#!/usr/bin/env python
# coding: utf-8
import os
import sys
import pickle
import pandas as pd
import argparse
import dotenv

dotenv.load_dotenv()


def prepare_data(df, categorical):
    df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df["duration"] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[categorical] = df[categorical].fillna(-1).astype("int").astype("str")
    return df


def read_data(filename, categorical):
    S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
    if S3_ENDPOINT_URL is not None:
        options = {"client_kwargs": {"endpoint_url": S3_ENDPOINT_URL}}
        # print(filename)
        df = pd.read_parquet(filename, storage_options=options)
    else:
        df = pd.read_parquet(filename)

    df = prepare_data(df, categorical)
    return df


def save_data(df, save_path):
    S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")

    if S3_ENDPOINT_URL is not None:
        options = {
            "client_kwargs": {
                "endpoint_url": S3_ENDPOINT_URL,
            },
        }

        df.to_parquet(
            save_path,
            engine="pyarrow",
            compression=None,
            index=False,
            storage_options=options,
        )
    else:
        print("Can't save to s3 cuz no S3_ENDPOINT_URL environment variable found!")
        df.to_parquet(
            save_path,
            engine="pyarrow",
            index=False,
        )


def get_input_path(year, month):
    default_input_pattern = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet"
    input_pattern = os.getenv("INPUT_FILE_PATTERN", default_input_pattern)
    return input_pattern.format(year=year, month=month)


def get_output_path(year, month):
    default_output_pattern = (
        "s3://nyc-duration/predictions_{month:02d}_{year:04d}.parquet"
    )
    output_pattern = os.getenv("OUTPUT_FILE_PATTERN", default_output_pattern)
    return output_pattern.format(year=year, month=month)


def main(year, month):
    # pylint: disable=invalid-name

    input_file = get_input_path(year, month)
    output_file = get_output_path(year, month)
    print(input_file)
    print(output_file)
    with open("model.bin", "rb") as f_in:
        dv, lr = pickle.load(f_in)

    categorical = ["PULocationID", "DOLocationID"]

    df = read_data(input_file, categorical)
    df["ride_id"] = f"{year:04d}/{month:02d}_" + df.index.astype("str")

    dicts = df[categorical].to_dict(orient="records")
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)

    print("predicted mean duration:", y_pred.mean())

    df_result = pd.DataFrame()
    df_result["ride_id"] = df["ride_id"]
    df_result["predicted_duration"] = y_pred

    save_data(df_result, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", default=2023, type=int)
    parser.add_argument("-m", "--month", default=3, type=int)
    args = parser.parse_args()
    main(year=args.year, month=args.month)
