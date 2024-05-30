# import base64
# import io
# from typing import Tuple

# import matplotlib.pyplot as plt
# import numpy as np
# import shap
# from pandas import Series
# from scipy.sparse._csr import csr_matrix
# from xgboost import DMatrix
# import xgboost as xgb



# def create_visualization():
#     n = 10
    
#     X = np.random.rand(n,4)
#     y = np.random.rand((n))
#     model = xgb.train(
#         params={

#         },
#         dtrain=DMatrix(X,y),
#     )

#     # Random sampling - for example, 10% of the data
#     sample_indices = np.random.choice(X.shape[0], size=int(X.shape[0] * 0.1), replace=False)
#     X_sampled = X[sample_indices]
#     X_sampled = X[:1]
#     X_sampled = np.array(X_sampled)
#     print(X_sampled.shape)
#     print(type(model))
#     # Now, use X_sampled instead of X for SHAP analysis
#     explainer = shap.TreeExplainer(model)
#     shap_values = explainer.shap_values(X_sampled)
#     shap.summary_plot(shap_values, X_sampled, plot_type='bar')

#     my_stringIObytes = io.BytesIO()
#     plt.savefig(my_stringIObytes, format='jpg')
#     my_stringIObytes.seek(0)
#     my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

#     plt.close()

#     return my_base64_jpgData
# create_visualization()
# from mage_ai.data_preparation.models.global_data_product import GlobalDataProduct
from mage_ai.data_preparation.variable_manager import get_variable

# training_set = GlobalDataProduct
training_set = get_variable('xgboost_training',"training_set","")
print(type(training_set))
print(training_set)
# print(training_set.keys())
# print(type(training_set['build']))
# print(training_set['remote_blocks'][0].keys())
# X, X_train, X_val, y, y_train, y_val, _ = training_set["build"]['']
# print(X.shape,X_train.shape)