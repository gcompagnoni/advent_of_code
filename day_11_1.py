import numpy as np
from scipy.signal import convolve2d

with open('inputs/input_11.txt', 'r') as infile:
    start_array = np.array([list(l) for l in infile.read().split()])

# computing the sum of neighbours is the same as applying a convolution with the following kernel
ker = np.ones((3, 3), dtype=np.int)
ker[1, 1] = 0

old_seats = np.empty_like(start_array)
new_seats = start_array

while (old_seats != new_seats).any():
    old_seats = new_seats.copy()
    free_seats = (old_seats == 'L')
    full_seats = (old_seats == '#')

    num_full_nb = convolve2d(full_seats, ker, mode='same')

    new_seats[free_seats & (num_full_nb == 0)] = '#'
    new_seats[full_seats & (num_full_nb >= 4)] = 'L'

print(full_seats.sum())
