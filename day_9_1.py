from typing import List

with open('inputs/input_9.txt', 'r') as infile:
    input_lines = infile.readlines()

numbers = [int(x) for x in input_lines]


def in_sumset(n: int, s: List[int]) -> bool:
    for x in s:
        y = n - x
        if y in s and x != y:
            return True
    return False


for k in range(25, len(numbers)):
    if not in_sumset(numbers[k], numbers[k - 25:k]):
        print(numbers[k])
        break