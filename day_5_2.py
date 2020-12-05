from typing import Tuple

with open('inputs/input_5.txt', 'r') as infile:
    seat_list = infile.read().split()


def str2place(input_string: str) -> Tuple[int, int]:
    row_binary = input_string[:7].replace('F', '0').replace('B', '1')
    col_binary = input_string[7:].replace('L', '0').replace('R', '1')
    return int(row_binary, 2), int(col_binary, 2)


seat_ids = set()
for seat in seat_list:
    row_num, col_num = str2place(seat)
    seat_id = 8 * row_num + col_num  # this is the same as just reading the whole string as binary
    seat_ids.add(seat_id)

no_front = set(range(min(seat_ids)))
no_back = set(range(max(seat_ids) + 1, 2 ** 10))
my_seat = set(range(2 ** 10)).difference(seat_ids).difference(no_front).difference(no_back)

print(my_seat)
