"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""

from mage_ai.data_preparation.variable_manager import get_variable


model = get_variable('xgboost_training', 'dashboard_data_source', 'output_0')
X = get_variable('xgboost_training', 'dashboard_data_source', 'output_1')
y = get_variable('xgboost_training', 'dashboard_data_source', 'output_2')
all_data = (model, X, y)

print(type(model))
print(type(X))
print(type(y))
print(type(all_data))


import base64
import io
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import shap
from pandas import Series
from scipy.sparse import csr_matrix
from xgboost import Booster,DMatrix


def create_visualization(
    inputs: Tuple[Booster, csr_matrix, Series],
    **kwargs,
) -> str:

    model, X, y = inputs

    sample_indices = np.random.choice(
        X.shape[0],
        size=int(X.shape[0]*0.1),
        replace=False,       
    )

    X_sampled = X[sample_indices]
    X_sampled = X[:1]
    X_sampled = X_sampled.toarray()
    print(type(model))
    print(X_sampled.shape)
    # Now explain
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sampled)
    shap.summary_plot(shap_values, X_sampled)

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(
        my_stringIObytes.read(),
    ).decode()

    # plt.close()

    return None

create_visualization(all_data)
# dmatrix_props = getattr(model, "_xgb_dmatrix_props", {})
# dmat = DMatrix(X, **dmatrix_props)
# model.predict(dmat)