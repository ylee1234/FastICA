import numpy as np


def compute_distance(x,y):
    x1=np.abs(x)
    y1=np.abs(y)
    return np.sum(np.abs(x1-y1))