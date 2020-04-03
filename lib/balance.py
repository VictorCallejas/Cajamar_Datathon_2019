import pandas as pd

from imblearn.combine import SMOTETomek
from imblearn.combine import SMOTEENN

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import seaborn as sns

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Revisa esto
"""
def getRatios(y, multiplicador):
    count = y.value_counts().sum()
    classes_count = y.value_counts()
    ratio_classes={
            1: int(((1-(classes_count[1]/count))*multiplicador)),
            2: int((100-(classes_count[2]/count))*multiplicador),
            3: int((100-(classes_count[3]/count))*multiplicador),
            4: int((100-(classes_count[4]/count))*multiplicador),
            5: int((100-(classes_count[5]/count))*multiplicador),
            6: int((100-(classes_count[6]/count))*multiplicador),
            7: int((100-(classes_count[7]/count))*multiplicador)
        }
    return ratio_classes
"""
"""
def balanceSMOTETomek(X,y, ratio='auto'):
    ratio_classes = getRatios(y, suavizador)
    smote_tomek = SMOTETomek(random_state=0,n_jobs=12,sampling_strategy=ratio_classes)
    X_resampled, y_resampled = smote_tomek.fit_resample(X, y)
"""