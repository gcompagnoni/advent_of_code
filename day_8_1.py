with open('inputs/input_8.txt', 'r') as infile:
    lines = infile.readlines()

accumulator = 0


def execute_line(line_num: int) -> int:
    line = lines[line_num]
    instruction = line[:3]
    number = int(line[4:-1])
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


new_line = 0
visited_lines = {new_line}
visited = False

while not visited:
    new_line = execute_line(new_line)
    visited = new_line in visited_lines
    visited_lines.add(new_line)

print(accumulator)
