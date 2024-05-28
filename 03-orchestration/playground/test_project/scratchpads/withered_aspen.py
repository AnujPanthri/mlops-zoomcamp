"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable
from test_project.utils.data_preparation.cleaning import clean
from test_project.utils.data_preparation.feature_engineering import combine_features
from test_project.utils.data_preparation.feature_selector import select_features
from test_project.utils.data_preparation.splitters import split_on_value


df = get_variable('data_preparation', 'prepare', 'output_0')
print(type(df))
print(len(df))
print(type(df[0]))
print(len(df[0]))