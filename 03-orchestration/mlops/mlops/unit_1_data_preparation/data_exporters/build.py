from typing import Tuple
from pandas import DataFrame, Series
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator
from sklearn.feature_extraction import DictVectorizer
from mlops.utils.data_preparation.feature_selector import select_features
from mlops.utils.data_preparation.encoders import vectorize_features


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
    from mage_ai.data_preparation.decorators import test


@data_exporter
def export_data(
    data: Tuple[DataFrame, DataFrame, DataFrame],
    **kwargs
) -> Tuple[
    csr_matrix,
    csr_matrix,
    csr_matrix,
    Series,
    Series,
    Series,
    BaseEstimator,
]:

    df, df_train, df_val = data
    target = kwargs.get("target")
    # vectorize features
    X, _, _ = vectorize_features(select_features(df))
    y: Series = df[target]

    X_train, X_val, dv = vectorize_features(
        select_features(df_train), 
        select_features(df_val)
        )

    y_train:Series = df_train[target]
    y_val:Series = df_val[target]

    return X, X_train, X_val, y, y_train, y_val, dv

@test
def test_dataset(
    X: csr_matrix,
    X_train: csr_matrix,
    X_val: csr_matrix,
    y: Series,
    y_train: Series,
    y_val: Series,
    dv: BaseEstimator,
    *args,
) -> None:
    
    assert X.shape[0] == 105870
    assert X.shape[1] == 7027

    assert len(y.index) == X.shape[0]

@test
def test_train_dataset(
    X: csr_matrix,
    X_train: csr_matrix,
    X_val: csr_matrix,
    y: Series,
    y_train: Series,
    y_val: Series,
    dv: BaseEstimator,
    *args,
) -> None:
    
    assert (
        X_train.shape[0] == 54378
    ), f"Training set for training model should have 54378 examples, but has {X_train.shape[0]}"
    
    assert (
        X_train.shape[1] == 5094
    ), f"Training set for training model should have 5094 features, but has {X_train.shape[1]}"

    assert (
        len(y_train.index) == X_train.shape[0]
    ), f"Training set(y_train) for training model should have {X_train.shape[0]} examples, but has {len(y_train.index)}"

@test
def test_validation_dataset(
    X: csr_matrix,
    X_train: csr_matrix,
    X_val: csr_matrix,
    y: Series,
    y_train: Series,
    y_val: Series,
    dv: BaseEstimator,
    *args,
) -> None:
    
    assert (
        X_val.shape[0] == 51492
    ), f"Validation set for validation should have 51492 examples, but has {X_val.shape[0]}"
    
    assert (
        X_val.shape[1] == 5094
    ), f"Validation set for validation should have 5094 features, but has {X_val.shape[1]}"

    assert (
        len(y_val.index) == X_val.shape[0]
    ), f"Validation set(y_val) for validation should have {X_val.shape[0]} examples, but has {len(y_val.index)}"