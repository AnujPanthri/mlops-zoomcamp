import pandas as pd
from typing import Union,List,Dict,Optional,Tuple
from test_project.utils.data_preparation.cleaning import clean
from test_project.utils.data_preparation.feature_engineering import combine_features
from test_project.utils.data_preparation.feature_selector import select_features
from test_project.utils.data_preparation.splitters import split_on_value

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(
    df:pd.DataFrame,
    **kwargs,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    split_on_feature = kwargs.get("split_on_feature")
    split_on_feature_value = kwargs.get("split_on_feature_value")
    target = kwargs.get("target")

    # df = df.iloc[:100]
    df = clean(df)
    df = combine_features(df)
    df = select_features(df,features=[split_on_feature, target])

    df_train, df_val = split_on_value(
        df,
        split_on_feature,
        split_on_feature_value,
    )

    
    return df, df_train, df_val


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
    
#     # assert isinstance(output,Tuple)
#     # assert len(output)==3
#     # assert isinstance(output[0],pd.DataFrame)
#     # assert isinstance(output[1],pd.DataFrame)
#     # assert isinstance(output[2],pd.DataFrame)
