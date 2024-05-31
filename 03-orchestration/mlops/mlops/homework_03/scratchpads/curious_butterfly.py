import mlflow

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("yellow-taxi-duration")