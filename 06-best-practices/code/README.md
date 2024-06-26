```bash
aws --endpoint-url=http://localhost:4566 \
    kinesis list-streams
```

```bash
aws --endpoint-url=http://localhost:4566 \
    kinesis create-stream \
    --stream-name ride_predictions \
    --shard-count 1
```

```bash
export SHARD="shardId-000000000000"
export PREDICTIONS_STREAM_NAME="ride_predictions"
aws --endpoint-url=http://localhost:4566 \
    kinesis get-shard-iterator \
    --shard-id ${SHARD} \
    --shard-iterator-type TRIM_HORIZON \
    --stream-name ${PREDICTIONS_STREAM_NAME} \
    --query 'ShardIterator'
```

```bash
aws --endpoint-url=http://localhost:4566 \
    kinesis get-records \
    --shard-iterator "shard-iterator-id"
```

```bash
echo "eyJtb2RlbCI6ICJyaWRlX2R1cmF0aW9uX3ByZWRpY3Rpb25fbW9kZWwiLCAidmVyc2lvbiI6ICJUZXN0MTIzIiwgInByZWRpY3Rpb24iOiB7InJpZGVfZHVyYXRpb24iOiAyMS4yOTQ1NDUzNDgzMzM0MDgsICJyaWRlX2lkIjogMjU2fX0=" | base64 -d | jq
```