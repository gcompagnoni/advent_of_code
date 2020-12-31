import numpy as np
from scipy.signal import convolve

with open('inputs/input_17.txt', 'r') as infile:
    start_array = np.array([list(l) for l in infile.read().split()])
space = (start_array == '#')[:, :, None, None].astype(int)

num_cycles = 6
space = np.pad(space, num_cycles)

ker = np.ones((3, 3, 3, 3), dtype=int)
ker[1, 1, 1, 1] = 0

for _ in range(num_cycles):
    num_nbs = convolve(space, ker, mode='same')
    old_space = space.copy()
    space[(old_space == 1) & ((num_nbs < 2) | (num_nbs > 3))] = 0
    space[(old_space == 0) & (num_nbs == 3)] = 1

print(space.sum())
