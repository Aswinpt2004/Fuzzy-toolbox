import numpy as np

def fuzzy_union(muA, muB):
    return np.maximum(muA, muB)

def fuzzy_intersection(muA, muB):
    return np.minimum(muA, muB)

def fuzzy_complement(muA):
    return 1 - muA

def fuzzy_difference(muA, muB):
    return np.minimum(muA, 1 - muB)
