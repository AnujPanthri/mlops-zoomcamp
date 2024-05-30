if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(training_set, **kwargs):
    X, X_train, X_val, y, y_train, y_val, _ = training_set["build"]
    return X.shape, X_train.shape, X_val.shape

