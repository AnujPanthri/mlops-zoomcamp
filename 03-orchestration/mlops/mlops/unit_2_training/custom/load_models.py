from typing import Tuple, Dict, List

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def models(
    *args,
    **kwargs
) -> Tuple[List[str], List[Dict[str, str]]]:
    """
    models: comma separated strings
        linear_model.Lasso
        linear_model.LinearRegression
        svm.LinearSVR
        ensemble.ExtraTreesRegressor
        ensemble.GradientBoostingRegressor
        ensemble.RandomForestRegressor
    """
    
    model_names: str = kwargs.get(
        "models",
        "linear_model.Lasso, linear_model.LinearRegression"
    )

    child_data: List[str] = [
        model.strip() for model in model_names.split(",")
    ]
    child_metadata: List[Dict[str, str]] = [
        dict(block_uuid=model.split(".")[-1]) for model in child_data
    ]

    return child_data, child_metadata