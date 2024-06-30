#!/usr/bin/env bash

cd "$(dirname "$0")"

docker compose down
docker compose up -d

aws s3 mb s3://nyc-duration

python integration_test.py
