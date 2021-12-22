from scipy import constants as const
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = const.G
l = 5

theta0 = const.pi/2

w0 = 1

def f_func(state, time):
    f = np.zeros(2)
    f[0] = state[1]
    f[1] = (-g / l) * np.sin(state[0])

    return f

X0 = [theta0, w0]
t0 = 0

tf = 100
tau = 0.1

t = np.arange(t0,tf,tau)

X = odeint(f_func,X0,t)

theta = X[:,0]
w = X[:,1]

x_plt = np.cos(np.array(theta))
y_plt = np.sin(np.array(theta))

plt.plot(theta, w)
plt.show()


