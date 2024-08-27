from scipy import linalg
import numpy as np
import scipy as sp

def load_from_csv(filename):
    """load, read, filter data"""

def isempty(x):
    return len(x) == 0

class node:
    def __init__(self, u, f):
        self.u = u
        self.f = f    

class element:
    def __init__(self, k, cnt):
        self.k = k
        self.cnt = cnt
        coef = np.array([[1, -1],[-1, 1]])
        self.K = np.multiply(coef, k)
