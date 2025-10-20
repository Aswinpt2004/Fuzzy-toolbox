# modules/fuzzy_membership.py
import numpy as np
import skfuzzy as fuzz

def triangular(x, a, b, c):
    return fuzz.trimf(x, [a, b, c])

def trapezoidal(x, a, b, c, d):
    return fuzz.trapmf(x, [a, b, c, d])

def gaussian(x, mean, sigma):
    return fuzz.gaussmf(x, mean, sigma)

def gbell(x, a, b, c):
    """Generalized Bell MF"""
    return fuzz.gbellmf(x, a, b, c)

def sigmoidal(x, a, c):
    """Sigmoid MF"""
    return fuzz.sigmf(x, c, a)
