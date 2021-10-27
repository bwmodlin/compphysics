import numpy as np
import matplotlib.pyplot as plt

def euler(method):
    x0 = 1.0
    v0 = 0.0
    tau = 1.0
    w = 0.5

    x = x0
    v = v0
    t = 0.0

    x_plt = np.array([x])
    v_plt = np.array([v])
    t_plt = np.array([t])

    period = (1 / (w / 2*np.pi)) *10

    finalTime = period * 100


    if (method == "Euler"):
        while (t < finalTime):
            x = x + v*tau
            a = -w**2 * x
            v = v + a*tau
            t = t + tau

            x_plt = np.append(x_plt, x)
            v_plt = np.append(v_plt, v)
            t_plt = np.append(t_plt, t)
    
    elif (method == "Comer"):
        while (t < finalTime):
            a = -w**2 * x
            v = v + a*tau
            x = x + v*tau
            t = t + tau

            x_plt = np.append(x_plt, x)
            v_plt = np.append(v_plt, v)
            t_plt = np.append(t_plt, t)
    else:
        print("Not a valid method")
        return

    plt.figure(1)
    plt.plot(t_plt, x_plt)
    plt.plot(t_plt, v_plt)
    plt.legend(["Position Graph", "Velocity Graph"])
    title = "{}'s Method to Approximate Position and Velocity".format(method)
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m) / Velocity (m/s)")
    plt.title(title)

    plt.figure(2)
    plt.plot(x_plt, v_plt)
    plt.xlabel("Position (m)")
    plt.ylabel("Velocity (m/s)")
    title = "{}'s Method Phase Portrait".format(method)
    plt.title(title)

    plt.show()

euler("Comer")
euler("Euler")











