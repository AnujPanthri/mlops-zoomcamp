from typing import Callable, Dict, Tuple, Union

from pandas import Series
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator

from mlops.utils.models.sklearn import load_class, train_model
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def train(
    settings: Tuple[
        Dict[str, Union[bool, int, float, str]],
        csr_matrix,
        Series,
        Dict[str, Union[Callable[..., BaseEstimator], str]],
    ],
    *args,
    **kwargs,
) -> Dict[str, Union[BaseEstimator, Dict[str, str]]]:
    """
    train sklearn models with best hyperparameters
    """
    
    hyperparameters, X, y, model_info = settings

    model_class = model_info['cls']
    model = model_class(**hyperparameters)
    model.fit(X, y)

    return model, model_info