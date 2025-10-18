# modules/fuzzy_sets.py
import numpy as np
import skfuzzy as fuzz

# --- Membership Functions ---
def triangular(x, a, b, c):
    return fuzz.trimf(x, [a, b, c])

def trapezoidal(x, a, b, c, d):
    return fuzz.trapmf(x, [a, b, c, d])

def gaussian(x, mean, sigma):
    return fuzz.gaussmf(x, mean, sigma)

# --- Set Operations ---
def fuzzy_union(A, B):
    return np.fmax(A, B)

def fuzzy_intersection(A, B):
    return np.fmin(A, B)

def fuzzy_complement(A):
    return 1 - A
