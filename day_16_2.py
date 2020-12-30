import re
from typing import Callable

import numpy as np
from scipy.optimize import linear_sum_assignment

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

tickets = [[int(x) for x in l.split(',')] for l in text_groups[2].split('\n')[1:]]
valid_tickets = [t for t in tickets if all(any(rule(val) for rule in rules) for val in t)]

num_fields = len(valid_tickets[0])
assert all(len(t) == num_fields for t in valid_tickets)

acceptable_fields = [[f for f in range(num_fields) if all(rule(t[f]) for t in valid_tickets)]
                     for rule in rules]

# this is now a bipartite matching problem
adj = np.ones((num_fields, num_fields), dtype=int)
for i, fields in enumerate(acceptable_fields):
    adj[i, fields] = 0  # set existing edges to cost 0
_, right_fields = linear_sum_assignment(adj)

my_ticket = [int(x) for x in text_groups[1].split('\n')[1].split(',')]
dep_values = [my_ticket[k] for k in right_fields[:6]]

print(np.product(dep_values, dtype=np.int64))
