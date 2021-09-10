import numpy as np
import matplotlib.pyplot as plt

C02_ppm_MaunaLoa = np.load("Quiz1/data.npy")

num_years = (C02_ppm_MaunaLoa.size * 14) / 365

years = np.linspace(1981, 1981+num_years, C02_ppm_MaunaLoa.size)

plt.plot(years, C02_ppm_MaunaLoa)

best_fit = np.polyfit(years, C02_ppm_MaunaLoa, 1)

fit_func = np.poly1d(best_fit)

plt.plot(years, fit_func(years))

plt.xlabel("Years")

plt.ylabel("$C0_2$ Concentration (ppm)")

slope_text = str(round(best_fit[0], 2)) + " ppm / two weeks"

plt.title("$C0_2$ increases at " + slope_text + " at Mauna Loa")

plt.show()

# plt.savefig("mygraph.png")
