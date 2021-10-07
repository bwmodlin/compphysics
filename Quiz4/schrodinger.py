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


def e_equation(s):
    return (-v * ((s**2 / k_square) - 1))


s = np.linspace(-k, k, 10000)
l = left(s)
r = right(s)
z = zero(s)
nu = np.zeros(s.shape)

s1 = fsolve(zero, 2.8)
s2 = fsolve(zero, 5.5)
s3 = fsolve(zero, 8.2)

# s= 2.80780709, 5.5749446, 8.16336383

print(e_equation(s1))
print(e_equation(s2))
print(e_equation(s3))

# E= 1.43e-16, 9.24e-17, 1.49e-17


#plt.plot(s, l)
#plt.plot(s, r)
plt.plot(s, z)
plt.plot(s, nu)


plt.ylim([-100, 100])
plt.show()
