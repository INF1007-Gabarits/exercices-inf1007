#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import scipy.integrate as integrate
import math


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray :
    return np.linspace(-1.3, 2.5, num = 64)

def coordinate_conversion(cartesian_coordinates : np.ndarray) -> np.ndarray:
    # x**2 + y**2 = r**2
    # theta = atan(y/x)
    answer = []
    
    for c in range(len(cartesian_coordinates)) :
        x = cartesian_coordinates[c][0]
        y = cartesian_coordinates[c][1]
        radius = math.sqrt(x**2 + y**2)
        angle = math.degrees(np.atan(y/x))
        answer.append((radius, angle))
    
    return np.array(answer)


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.argmin(np.abs(values - number))


def f(x : float) :
    return x**2 * np.sin(1/x**2) + x

def traceFunction(interval = [-1, 1], n = 250, function = f) :
    #fig, ax = plt.figure(figsize = (10, 10))
    x = np.linspace(interval[0], interval[1], n)
    y = function(x)
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Ma fonction affichée")
    plt.show()

def g(x) :
    return np.exp(-x**2)

def evaluateIntegral(intervalGraph = [-4, 4], function = g) :
    x = np.arange(intervalGraph[0], intervalGraph[1], 0.1)
    resultInt = integrate.quad(function, -np.inf, np.inf)
    
    y = [integrate.quad(function, 0, value)[0] for value in x]

    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Integrate e^-(x^2)")
    plt.show()

    return resultInt


def monteCarlo(iterations : int = 5000, radius = 1) :
    x_generated = np.random.rand()
    y_generated = np.random.rand()

    xIns = []
    xOut = []
    yIns = []
    yOut = []

    for i in range(iterations) :
        x = np.random.random()
        y = np.random.random()
        
        cond = np.sqrt(x**2 + y**2) <= 1.0
        if cond :
            # Nous sommes à l'intérieur du cercle.
            xIns.append(x)
            yIns.append(y)
        else :
            # Nous sommes à l'extérieur du cercle.
            xOut.append(x)
            yOut.append(y)
        
    plt.scatter(xIns, yIns)
    plt.scatter(xOut, yOut)
    plt.show()

    approxPi = len(xIns)/iterations * 4
    return approxPi
    

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([(1, 10), (-10, 105), (90.5, 182.1902), (102374.2347189, 347819.273481)])))
    
    traceFunction()
    #evaluateIntegral(intervalGraph = [-4, 10000])
    print(monteCarlo(10**5))
