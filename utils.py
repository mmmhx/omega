from scipy import linalg
import numpy as np
import scipy as sp

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

def n_nodes(nodes):
    x = len(nodes)
    return x,x

def BUILD_K(elements, nnodes):
    K = np.zeros(nnodes)
    for element in elements:
        for i in range(len(element.cnt)):
            for j in range(len(element.cnt)):
                K[element.cnt[i] - 1, element.cnt[j] - 1] += element.K[i - 1,j - 1]
    return K

def BUILD_F(nodes):
    nnodes = len(nodes)
    F = np.zeros(nnodes)
    i = 0
    for node in nodes:
        F[i] = node.f
        i += 1
    return F

def BUILD_U(nodes):
    nnodes = len(nodes)
    U = np.zeros(nnodes)
    i = 0
    for node in nodes:
        U[i] = node.u
        i += 1
    return U
