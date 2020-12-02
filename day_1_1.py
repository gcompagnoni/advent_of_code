from typing import List, Optional

with open('inputs/input_1.txt', 'r') as infile:
    s = [int(x) for x in infile.readlines()]

s.sort()
my_sum = 2020


def recursive_binary_search(r: List[int, ...], x: int) -> Optional[int]:
    if len(r) == 0:
        return None
    y_index = len(r) // 2
    y = r[y_index]
    if x + y == my_sum:
        return y
    elif x + y < my_sum:
        return recursive_binary_search(r[y_index + 1:], x)
    elif x + y > my_sum:
        return recursive_binary_search(r[:y_index], x)


for k, x in enumerate(s):
    y = recursive_binary_search(s[k + 1:], x)
    if y is not None:
        print(x, y, x * y)
        break
