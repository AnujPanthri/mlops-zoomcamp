import os
import boto3
import json
from deepdiff import DeepDiff
from pprint import pprint

endpoint_url = os.getenv("KINESIS_ENDPOINT_URL", "http://localhost:4566")
kinesis_client = boto3.client('kinesis', endpoint_url=endpoint_url)

stream_name = os.getenv("PREDICTIONS_STREAM_NAME", "ride_predictions")
shard_id = "shardId-000000000000"

shard_iterator_response = kinesis_client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType="TRIM_HORIZON",
)

shard_iterator_id = shard_iterator_response["ShardIterator"]

records_response = kinesis_client.get_records(
    ShardIterator=shard_iterator_id,
    Limit=1,
)

records = records_response['Records']
pprint(records)

assert len(records)==1

actual_record = json.loads(records[0]["Data"])
pprint(actual_record)

with open("prediction.json", "r", encoding="utf-8") as f_in:
    expected_record = json.load(f_in)

diff = DeepDiff(actual_record, expected_record, significant_digits=1)
print("diff:",diff)

assert 'type_changes' not in diff
assert 'values_changed' not in diff