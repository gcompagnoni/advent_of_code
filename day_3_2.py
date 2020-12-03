from math import ceil

import numpy as np

with open('inputs/input_3.txt', 'r') as infile:
    base_array = np.array([list(l) for l in infile.read().split()])

deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
prod = 1

for delta_x, delta_y in deltas:
    num_repetition = ceil(delta_x * base_array.shape[0] / (delta_y * base_array.shape[1]))
    full_array = np.tile(base_array, num_repetition)

    num_trees = 0

    for k in range(int((base_array.shape[0] - 1) / delta_y) + 1):
        if full_array[k * delta_y, k * delta_x] == '#':
            num_trees += 1
    prod *= num_trees
    print(num_trees)

print(prod)
