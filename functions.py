import math
import pylab
import numpy

def f(x, coefficient = 1, exponent = 1, h = 0, k = 0):
    '''
    Function representation of f(x) that can include a desired exponent, as
    well as transformations such as translations, and compressions

    Ex. f(x) = x, f(x, 2, 2) = 2x^2, f(x, 2, 2, 1, 5) = 2(x - 1)^2 + 5
        f(x, k = 1) = x + 1
    '''
    
    return coefficient * ((x - h) ** exponent) + k


def g(x, base, k = 0):
    '''
    Function representation as an exponential function

    Ex. g(x, math.e) = e^x
    '''

    return base ** x + k


def quadratic(x, a, b, c):
    # Function representation of a basic quadratic function

    return a * (x ** 2) + b * x + c


def log(x, base = math.e, coefficient = 1):
    # Represents logarithmic functions

    return coefficient * (math.log(x) / math.log(base))


def compose(f, g):
    # Takes two functions and returns their composition

    return f(g(x))


def plot_func(f, lower_bound = -10, upper_bound = 10, increment = 0.1):
    # Plots the given function over the given range and increment

    X = numpy.arange(lower_bound, upper_bound, increment)
    Y = []

    for x in X:
        Y.append(f(x))

    pylab.plot(X,Y)
    pylab.show()
