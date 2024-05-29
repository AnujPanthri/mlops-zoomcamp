from typing import Callable, Dict, Tuple, Union
from pandas import Series
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator

from mlops.utils.models.sklearn import load_class, tune_hyperparameters

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def testing(
    model_class_name: str,
    training_set: Dict[str, Union[Series,csr_matrix]],
    *args,
    **kwargs,
) -> str:
    """
    perform hyperparameter tuning on sklearn models
    """
    
    return model_class_name
dd