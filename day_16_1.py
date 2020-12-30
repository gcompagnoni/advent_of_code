import re
from typing import Callable

with open('inputs/input_16.txt', 'r') as infile:
    text_groups = infile.read().split('\n\n')


def read_rule(rule_text: str) -> Callable[[int], bool]:
    bounds_list = [range(int(x), int(y) + 1) for (x, y) in
                   re.findall('([0-9]+)-([0-9]+)', rule_text)]
    return lambda n: any(n in b for b in bounds_list)


rules = []
for line in text_groups[0].split('\n'):
    if '-' in line:
        rules.append(read_rule(line))

values = [int(x) for x in re.findall('[0-9]+', text_groups[2])]
invalid_fields = [val for val in values if not any(rule(val) for rule in rules)]

print(sum(invalid_fields))
