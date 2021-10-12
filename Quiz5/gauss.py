from pylab import *
from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const

stddev = 5
mean = 0


def gauss(x):
    return (1 / (stddev * np.sqrt(2 * const.pi))) * np.exp((-1/2)*(((x-mean)**2)/stddev))
