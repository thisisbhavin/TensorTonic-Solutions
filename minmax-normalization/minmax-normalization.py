import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    min_X = X.min(axis=axis, keepdims=True)
    max_X = X.max(axis=axis, keepdims=True)
    scaled_X = (X - min_X) / (max_X - min_X + eps)
    return scaled_X
    