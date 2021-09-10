import numpy as np
import matplotlib.pyplot as plt

C02_ppm_MaunaLoa = np.load("data.npy")

num_years = (C02_ppm_MaunaLoa.size * 14) / 365

years = np.linspace(1981, 1981+num_years, C02_ppm_MaunaLoa.size)

plt.plot(years, C02_ppm_MaunaLoa)

best_fit = np.polyfit(years, C02_ppm_MaunaLoa, 1)

fit_func = np.poly1d(best_fit)

plt.plot(years, fit_func(years))

plt.show()
