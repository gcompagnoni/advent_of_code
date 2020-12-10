from typing import Tuple


def interpret_line(line: str) -> Tuple[int, int, str, str]:
    line = line.split()
    min_char, max_char = [int(k) for k in line[0].split('-')]
    char = line[1][0]
    string = line[2]
    return min_char, max_char, char, string


with open('inputs/input_2.txt', 'r') as infile:
    input_list = infile.readlines()

valid_lines = 0

for line in input_list:
    min_char, max_char, char, string = interpret_line(line)
    num_char = string.count(char)
    if min_char <= num_char <= max_char:
        valid_lines += 1

print(valid_lines)
