# modules/fuzzy_relations.py
import numpy as np

def max_min_composition(R, S):
    """
    Perform max-min composition of two fuzzy relations R(x, y) and S(y, z)
    """
    m, n = R.shape
    n2, p = S.shape
    assert n == n2, "Number of columns in R must equal rows in S"

    T = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            T[i, j] = np.max(np.minimum(R[i, :], S[:, j]))
    return T

def max_product_composition(R, S):
    """
    Perform max-product composition of two fuzzy relations R(x, y) and S(y, z)
    """
    m, n = R.shape
    n2, p = S.shape
    assert n == n2, "Number of columns in R must equal rows in S"

    T = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            T[i, j] = np.max(R[i, :] * S[:, j])
    return T

def random_relation(rows, cols):
    """
    Generate a random fuzzy relation matrix (values ∈ [0,1])
    """
    return np.round(np.random.rand(rows, cols), 2)
