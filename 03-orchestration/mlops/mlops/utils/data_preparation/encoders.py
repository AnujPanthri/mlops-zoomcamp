from typing import Union, List, Dict, Optional,Tuple

from pandas import DataFrame, Series
from scipy.sparse import csr_matrix
from sklearn.feature_extraction import DictVectorizer

def vectorize_features(
    training_set: DataFrame,
    validation_set: Optional[DataFrame] = None,
) -> Tuple[
    csr_matrix,
    csr_matrix,
    DictVectorizer,
]:
    
    # fit an DictVectorizer on training set
    dv = DictVectorizer()

    train_dicts = training_set.to_dict(orient="records")
    X_train = dv.fit_transform(train_dicts)

    X_val = None
    if validation_set is not None:
        val_dicts = validation_set.to_dict(orient="records")
        X_val = dv.transform(val_dicts)

    return X_train, X_val, dv