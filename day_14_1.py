import re

import numpy as np

with open('inputs/input_14.txt', 'r') as infile:
    lines = infile.read().split('\n')


def apply_mask(mask: str, num: int) -> int:
    mask_ar = np.array(list(mask))
    num_bin = bin(int(num))[2:]  # binary numbers start with 0b prefix
    num_ar = np.array(['0'] * (36 - len(num_bin)) + list(num_bin))
    num_ar[mask_ar != 'X'] = mask_ar[mask_ar != 'X']
    return int(''.join(num_ar), 2)


memory = {}
for line in lines:
    if line.startswith('mask'):
        mask = re.findall('[01X]+', line)[0]
    elif line.startswith('mem'):
        address, value = re.findall('[0-9]+', line)
        memory[address] = apply_mask(mask, value)

print(sum([v for v in memory.values()]))
