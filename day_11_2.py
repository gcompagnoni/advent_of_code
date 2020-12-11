from typing import List

import numpy as np

with open('inputs/input_11.txt', 'r') as infile:
    start_array = np.array([list(l) for l in infile.read().split()])


def sight_lines(m: int, n: int, array: np.ndarray) -> List[np.ndarray]:
    lines = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            elif dx == 0:
                lines.append(array[m::dy, n][1:])
            elif dy == 0:
                lines.append(array[m, n::dx][1:])
            else:
                lines.append(array[m::dy, n::dx].diagonal()[1:])

    return [d for d in lines if len(d) > 0]


def first_nb(m: int, n: int, array: np.ndarray) -> List[str]:
    lines = sight_lines(m, n, array)
    return [d[(d != '.').nonzero()[0][0]] for d in lines if len((d != '.').nonzero()[0]) > 0]


old_seats = np.empty_like(start_array)
new_seats = start_array

while (old_seats != new_seats).any():
    old_seats = new_seats.copy()
    for M in range(old_seats.shape[0]):
        for N in range(old_seats.shape[1]):
            nb = first_nb(M, N, old_seats)
            if old_seats[M, N] == 'L' and nb.count('#') == 0:
                new_seats[M, N] = '#'
            elif old_seats[M, N] == '#' and nb.count('#') >= 5:
                new_seats[M, N] = 'L'

print((new_seats == '#').sum())
