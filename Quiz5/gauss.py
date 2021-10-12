from pylab import *
from scipy.integrate import quad
import numpy as np
import scipy.constants as const

stddev = 5
mean = 0


def gauss(x):
    return (1 / (stddev * np.sqrt(2 * const.pi))) * np.exp((-1/2)*(((x-mean)**2)/stddev**2))


def getProbability(low, high):
    integral = quad(gauss, low, high)
    print("Probability: {0:.5f}%".format(integral[0]*100))


x_low = 0
x_high = 10

getProbability(x_low, x_high)
