import base64
import io
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from pandas import Series
from scipy.sparse._csr import csr_matrix
from xgboost import Booster, DMatrix
import seaborn as sns

@render(render_type='jpeg')
def create_visualization(inputs: Tuple[Booster, csr_matrix, Series], **kwargs):
    model, X, y = inputs

    # Random sampling - for example, 10% of the data
    sample_indices = np.random.choice(X.shape[0], size=int(X.shape[0] * 0.1), replace=False)
    X_sampled = X[sample_indices]
    y_pred = model.predict(DMatrix(X_sampled))

    X_sampled = np.array(X_sampled)
    y_sampled = y.to_numpy()[sample_indices]

    
    bins = 20
    
    plt.figure()
    
    plt.title("Duration distribution plot")
    chart = sns.displot(
        (y_sampled,y_pred),
        # bins=bins,
        kde=True,
        # color="green",
        # label="y_true",
    )
    # chart = sns.displot(
    #     y_pred,
    #     # bins=bins,
    #     kde=True,
    #     color="green",
    #     # label="y_true",
    # )
    
    plt.xlabel("duration(in minutes)")
    plt.ylabel("Frequency")
    # plt.legend()

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

    plt.close()

    # return my_base64_jpgData