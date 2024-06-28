from pathlib import Path

from model import ModelService, base64_decode


def read_text(file):
    test_directory = Path(__file__).parent

    with open(test_directory / file, "r", encoding="utf-8") as f_in:
        return f_in.read().strip()


def test_prepare_features():
    ride = {
        "PULocationID": 130,
        "DOLocationID": 205,
        "trip_distance": 3.66,
    }
    model_service = ModelService(None)
    actual_features = model_service.prepare_features(ride)
    expected_features = {
        "PU_DO": "130_205",
        "trip_distance": 3.66,
    }

    assert actual_features == expected_features


def test_base64_decode():

    encoded_data = read_text("data.b64")

    actual_result = base64_decode(encoded_data)
    expected_result = {
        "ride": {
            "PULocationID": 130,
            "DOLocationID": 205,
            "trip_distance": 3.66,
        },
        "ride_id": 256,
    }

    assert actual_result == expected_result


class ModelMock:
    def __init__(self, value):
        self.value = value

    def predict(self, X):
        n = len(X)
        return [self.value] * n


def test_predict():
    model = ModelMock(10)
    model_service = ModelService(model)

    features = {
        "PU_DO": "130_205",
        "trip_distance": 3.66,
    }

    actual_prediction = model_service.predict(features)
    expected_prediction = 10.0

    assert actual_prediction == expected_prediction


def test_lambda_handler():
    model = ModelMock(10.0)
    model_version = "Test123"
    model_service = ModelService(model, model_version)

    base64_input = read_text("data.b64")

    event = {
        "Records": [
            {
                "kinesis": {
                    "data": base64_input,
                },
            }
        ],
    }

    actual_predictions = model_service.lambda_handler(event)
    expected_predictions = {
        'predictions': [
            {
                'model': 'ride_duration_prediction_model',
                'version': model_version,
                'prediction': {
                    'ride_duration': 10.0,
                    'ride_id': 256,
                },
            }
        ]
    }

    assert actual_predictions == expected_predictions
