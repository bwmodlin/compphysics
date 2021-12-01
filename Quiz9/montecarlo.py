import random
import numpy as np

radius = 5

n_total = 100000

area_of_square = 4 * radius**2
area_of_circle = np.pi * radius**2

in_circle = 0

# (0, 0) at center of square/circle
for i in range(n_total):
    guess_x = random.uniform(-radius, radius+1)
    guess_y = random.uniform(-radius, radius+1)

    # x^2 + y^2 = r^2
    if guess_x**2 + guess_y**2 <= radius**2:
        in_circle += 1

# in_circle / n_total = area_of_circle / area_of_square

guess_area = (float(in_circle) / float(n_total)) * float(area_of_square)

print(guess_area)
print(area_of_circle)