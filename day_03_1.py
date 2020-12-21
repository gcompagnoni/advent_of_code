from math import ceil

import numpy as np

with open('inputs/input_03.txt', 'r') as infile:
    base_array = np.array([list(l) for l in infile.read().split()])

delta_x = 3
delta_y = 1

num_repetition = ceil(delta_x * base_array.shape[0] / (delta_y * base_array.shape[1]))
full_array = np.tile(base_array, num_repetition)

num_trees = 0

for k in range(int(base_array.shape[0] / delta_y)):
    if full_array[k, k * delta_x] == '#':
        num_trees += 1

print(num_trees)
