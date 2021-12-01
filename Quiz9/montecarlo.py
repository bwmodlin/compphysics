import random
import numpy as np
import matplotlib.pyplot as plt

radius = 5

area_of_square = 4 * radius**2
area_of_circle = np.pi * radius**2

n_total = np.logspace(1, 7, 20)
error = []

for i in range(len(n_total)):
    
    in_circle = 0

    # (0, 0) at center of square/circle
    for j in range(int(n_total[i])):
        
        guess_x = random.uniform(-radius, radius)
        guess_y = random.uniform(-radius, radius)

        # x^2 + y^2 = r^2
        if guess_x**2 + guess_y**2 <= radius**2:
            in_circle += 1

    guess_area = (float(in_circle) / float(n_total[i])) * float(area_of_square)

    error.append(abs(guess_area-area_of_circle))

plt.semilogx(n_total, error)
plt.show()
