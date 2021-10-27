import numpy as np
import matplotlib.pyplot as plt

x0 = 1.0
v0 = 0.0
tau = 0.1
w = 0.5

x = x0
v = v0
t = 0.0

x_plt = np.array([x])
v_plt = np.array([v])
t_plt = np.array([t])

while (t < 50):
    x = x + v*tau
    a = -w**2 * x
    v = v + a*tau
    t = t + tau

    x_plt = np.append(x_plt, x)
    v_plt = np.append(v_plt, v)
    t_plt = np.append(t_plt, t)

plt.plot(t_plt, x_plt)
plt.show()







