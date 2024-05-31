from typing import Tuple, Union, Dict

import os
import pickle
import mlflow

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def train_model(
    train_df: pd.DataFrame, 
    **kwargs,
) -> Tuple[
    DictVectorizer,
    LinearRegression,
    Dict[str,Union[int, float, str, bool]],
]:
    """
    train a DictVectorizer and an LinearRegression Model
    """
    
    # feature selection
    categorical = ["PULocationID", "DOLocationID"]
    numerical = []

    # # train a dict vectorizer
    # dv = DictVectorizer()
    # train_dicts = train_df[categorical+numerical].to_dict(orient="records")
    # X_train = dv.fit_transform(train_dicts)
    # y_train = train_df.duration

    # setup mlflow 
    
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("yellow-taxi-duration")
    # mlflow.set_experiment("random-forest-hyperopt")
    # print(mlflow.get_tracking_uri())
    # with mlflow.start_run():
    #     mlflow.log_param("model","linear_regression")
    #     # train model
    #     model = LinearRegression()
    #     model.fit(X_train, y_train)

    #     # evalulate model
    #     y_pred = model.predict(X_train)
    #     rmse = mean_squared_error(y_train,y_pred,squared=False)
    #     mse = mean_squared_error(y_train,y_pred)
    #     intercept = model.intercept_

    #     metrics={
    #         "rmse":rmse,
    #         "mse":mse,
    #         "intercept":intercept,
    #     }

    #     os.makedirs("preprocessing",exists_ok=True)
    #     with open("preprocessing/preprocessing.b",'wb') as f:
    #         pickle.dump(dv,f)

    #     mlflow.log_metrics(metrics)
    #     mlflow.sklearn.log_model(model,"model")
    #     mlflow.log_artifact(
    #         "preprocessing/preprocessing.b",
    #         artifact_path="preprocessing/preprocessing.b",

    #     )
        


    # return dv, model, metrics