import re
from typing import List, Optional

with open('inputs/input_08.txt', 'r') as infile:
    lines = infile.readlines()


def execute_line(line_num: int, line_list: List[str]) -> Optional[int]:
    try:
        line = line_list[line_num]
    except IndexError:
        return None  # the program terminated successfully
    instruction = line[:3]
    number = int(re.search('[+-][0-9]+', line).group())
    if instruction == 'nop':
        return line_num + 1
    elif instruction == 'jmp':
        return line_num + number
    elif instruction == 'acc':
        global accumulator
        accumulator += number
        return line_num + 1
    else:
        raise ValueError(f'Line {line_num}: unknown instruction')


def swap_instruction(line_num: int) -> Optional[List[str]]:
    new_line_list = lines.copy()
    instruction = new_line_list[line_num][:3]
    if instruction == 'acc':
        return None
    elif instruction == 'jmp':
        new_line_list[line_num] = 'nop' + new_line_list[line_num][3:]
    elif instruction == 'nop':
        new_line_list[line_num] = 'jmp' + new_line_list[line_num][3:]
    return new_line_list


for swap_num in range(len(lines)):
    new_lines = swap_instruction(swap_num)
    if new_lines is None:
        continue

    accumulator = 0
    new_line = 0
    visited_lines = {new_line}
    visited = False
    terminates = False

    while not visited:
        new_line = execute_line(new_line, new_lines)
        if new_line is None:
            terminates = True
            break
        visited = new_line in visited_lines
        visited_lines.add(new_line)

    if terminates:
        print(f'Changing line {swap_num} breaks the loop')
        print(f'Accumulator value: {accumulator}')
        break
