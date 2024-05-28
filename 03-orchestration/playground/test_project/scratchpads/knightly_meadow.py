"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable
from test_project.utils.data_preparation.cleaning import clean
from test_project.utils.data_preparation.feature_engineering import combine_features
from test_project.utils.data_preparation.feature_selector import select_features
from test_project.utils.data_preparation.splitters import split_on_value


df = get_variable('data_preparation', 'ingest', 'output_0')
print(type(df))
df = clean(df)
print(type(df))
df = combine_features(df)
print(type(df))
df = select_features(df,features=["lpep_pickup_datetime", "duration"])
print(type(df))

df_train, df_val = split_on_value(
    df,
    "lpep_pickup_datetime",
    "2024-02-01",
)

print("df_train:",type(df_train))
print("df_val:",type(df_val))