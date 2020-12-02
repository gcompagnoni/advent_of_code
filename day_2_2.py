from typing import Tuple


def interpret_line(line: str) -> Tuple[int, int, str, str]:
    line = line.split()
    place_1, place_2 = [int(k) for k in line[0].split('-')]
    char = line[1][0]
    string = line[2]
    return place_1, place_2, char, string


with open('inputs/input_2.txt', 'r') as infile:
    input_list = infile.readlines()

valid_lines = 0

for line in input_list:
    place_1, place_2, char, string = interpret_line(line)
    if (string[place_1 - 1] == char) != (string[place_2 - 1] == char):  # indices start from one
        valid_lines += 1

print(valid_lines)
