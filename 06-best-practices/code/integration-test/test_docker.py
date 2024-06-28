import json

import requests
from deepdiff import DeepDiff

with open("event.json", "r", encoding="utf-8") as f_in:
    event = json.load(f_in)

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
response = requests.post(url, json=event, timeout=10)
actual_response = response.json()
print(json.dumps(actual_response, indent=4))

with open("prediction.json", "r", encoding="utf-8") as f_in:
    expected_response = {"predictions": [json.load(f_in)]}

diff = DeepDiff(
    actual_response,
    expected_response,
    significant_digits=1,
)
print(f"diff:{diff}")

assert 'type_changes' not in diff
assert 'values_changed' not in diff
