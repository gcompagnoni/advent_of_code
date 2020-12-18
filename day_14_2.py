import re
from typing import List

import numpy as np

with open('inputs/input_14.txt', 'r') as infile:
    lines = infile.read().split('\n')


def apply_mask(mask: str, num: int) -> List[int]:
    mask_ar = np.array(list(mask))
    num_bin = bin(int(num))[2:]  # binary numbers start with 0b prefix
    num_ar = np.array(['0'] * (36 - len(num_bin)) + list(num_bin))
    num_ar[mask_ar == '1'] = '1'
    num_x = (mask_ar == 'X').sum()
    address_list = []
    for b in range(2 ** num_x):  # binary numbers < 2^n correspond to {0,1}^n
        b_bin = str(bin(b)[2:])
        b_seq = ['0'] * (num_x - len(b_bin)) + list(b_bin)
        address = num_ar.copy()
        address[mask_ar == 'X'] = b_seq
        address_list.append(int(''.join(address), 2))

    return address_list


memory = {}
for line in lines:
    if line.startswith('mask'):
        mask = re.findall('[01X]+', line)[0]
    elif line.startswith('mem'):
        address, value = re.findall('[0-9]+', line)
        for a in apply_mask(mask, address):
            memory[a] = int(value)

print(sum([v for v in memory.values()]))
