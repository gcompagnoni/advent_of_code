from typing import Tuple

with open('inputs/input_05.txt', 'r') as infile:
    seat_list = infile.read().split()


def str2place(input_string: str) -> Tuple[int, int]:
    row_binary = input_string[:7].replace('F', '0').replace('B', '1')
    col_binary = input_string[7:].replace('L', '0').replace('R', '1')
    return int(row_binary, 2), int(col_binary, 2)


seat_ids = set([(lambda s: 8 * s[0] + s[1])(str2place(seat)) for seat in seat_list])

possible_seats = set(range(min(seat_ids), max(seat_ids) + 1))
my_seat = possible_seats.difference(seat_ids)

print(my_seat)
