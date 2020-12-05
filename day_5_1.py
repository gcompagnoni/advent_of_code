from typing import Tuple

with open('inputs/input_5.txt', 'r') as infile:
    seat_list = infile.read().split()


def str2place(input_string: str) -> Tuple[int, int]:
    row_binary = input_string[:7].replace('F', '0').replace('B', '1')
    col_binary = input_string[7:].replace('L', '0').replace('R', '1')
    return int(row_binary, 2), int(col_binary, 2)


max_seat_id = 0
for seat in seat_list:
    row_num, col_num = str2place(seat)
    max_seat_id = max(max_seat_id, (8 * row_num + col_num))

print(max_seat_id)
