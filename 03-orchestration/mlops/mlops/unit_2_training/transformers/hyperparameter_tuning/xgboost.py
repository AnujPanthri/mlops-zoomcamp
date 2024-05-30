from typing import Dict, Tuple, Union

import numpy as np
import xgboost as xgb
from pandas import Series
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator

from mlops.utils.models.xgboost import build_data, tune_hyperparameters
from mlops.utils.logging import track_experiment
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(
    training_set: Dict[str, Union[csr_matrix, Series, BaseEstimator]],
    *args,
    **kwargs
) -> Tuple[
    Dict[str,Union[bool, int, float, str]],
    csr_matrix,
    csr_matrix,
]:
    """
    Hyperparameter tuning for xgboost model
    """

    # no need for DictVectorizer
    X, X_train, X_val, y, y_train, y_val, _ = training_set["build"]
    
    training = build_data(X_train, y_train)
    validation = build_data(X_val, y_val)

    best_hyperparameters = tune_hyperparameters(
        training,
        validation,
        callback = lambda **opts: track_experiment(**{**opts, **kwargs}),
        **kwargs,
        
    )

    return best_hyperparameters, X_train, y_train