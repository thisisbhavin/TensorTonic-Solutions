import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    X_mean = X.mean(axis=axis, keepdims=True)
    X_std = X.std(axis=axis, keepdims=True)
    return (X - X_mean) / (X_std + eps)