from typing import Dict, Tuple, Union

from pandas import Series
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator

from xgboost import Booster

from mlops.utils.models.xgboost import build_data, fit_model
from mlops.utils.logging import track_experiment
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(
    training_set: Dict[str, Union[csr_matrix, Series, BaseEstimator]],
    settings: Tuple[
        Dict[str,Union[bool, int, float, str]],
        csr_matrix,
        csr_matrix,
    ],
    *args,
    **kwargs
) -> Tuple[Booster, BaseEstimator]:
    """
    train xgboost model with best hyperparameters
    """
    
    # we don't need DictVectorizer
    X, X_train, X_val, y, y_train, y_val, dv = training_set["build"]
    hyperparameters, _, _ = settings

    # Test training a model with low max depth
    # so that the output renders a reasonable sized plot tree
    if kwargs.get("max_depth"):
        hyperparameters["max_depth"] = int(kwargs.get('max_depth'))

    # print(kwargs.get("max_depth"))
    model = fit_model(
        build_data(X_train,y_train),
        hyperparameters = hyperparameters,
        verbose_eval = kwargs.get("verbose_eval", 100),        
    )

    return model, dv
