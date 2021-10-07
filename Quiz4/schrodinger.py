import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

a = 0.529e-10
v = 1 * 10**3 * const.electron_volt
m = const.electron_mass
h = const.hbar

k_square = 2 * m * a**2 * v / (h**2)
k = np.sqrt(k_square)


def left(s):
    return (s * (1/np.tan(s)))


def right(s):
    return (- (np.sqrt(k_square-s**2)))


def zero(s):
    return (left(s) - right(s))


s = np.linspace(-k, k, 10000)
l = left(s)
r = right(s)
z = zero(s)
nu = np.zeros(s.shape)

print(fsolve(zero, 2.8))
print(fsolve(zero, 5.5))
print(fsolve(zero, 8.2))


# 2.80780709, 5.5749446, 8.16336383
#plt.plot(s, l)
#plt.plot(s, r)
plt.plot(s, z)
plt.plot(s, nu)


plt.ylim([-100, 100])
plt.show()
