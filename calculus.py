from functions import *

def derivative(function, x):
    # Takes in a function and an x-value and calculates its derivative
    
    dx = 0.0000000001

    return (function(x + dx) - function(x)) / dx


def integrate(function, a, b, N = 1000000):
    '''
    Takes in a function, a lower and upper bound, and a number of rectangles
    and adds them
    '''

    width = (b - a) / N
    totalArea = 0
    x = width

    for i in range(N):
        height = function(x)
        area = height * width
        totalArea += area
        x += width

    return totalArea
