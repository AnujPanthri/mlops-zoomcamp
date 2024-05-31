import mlflow

# mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("yellow-taxi-duration")