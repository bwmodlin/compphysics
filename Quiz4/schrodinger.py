import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


k_squared = 2 * const.electron_mass * \
    (0.529 * (10**(-10))) * (10**3) * const.electron_volt / const.hbar
k = np.sqrt(k_squared)

print(k)


def s_equation(s):
    eq = s * (1/np.tan(s)) + (np.sqrt(k**2 - s**2))
    return eq

# (s^2 / k^2) - 1 = - E / V0
# - V0 (s^2 / k^2) + V0 = E


def e_equation(s):
    return - 1 * 10 ** 3 * (s**2/k**2) + (10**3)


s = np.linspace(-k, k, 1000)
y = s_equation(s)
z = np.zeros(s.shape)

print(fsolve(s_equation, -6.9*10**(-12)))
print(fsolve(s_equation, 6.8*10**(-12)))

plt.figure(1)
plt.clf()

plt.plot(s, y, 'r--')

plt.xlabel('x')
plt.ylabel('cos(x)-exp(-x)')
plt.show()
