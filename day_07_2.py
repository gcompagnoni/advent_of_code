import re
from typing import Tuple, Dict, Optional

with open('inputs/input_07.txt', 'r') as infile:
    text_rules = infile.readlines()


def extract_rule(text_rule: str) -> Tuple[str, Optional[Dict]]:
    bag_list = [s for s in re.split('[\s]*bag[s]*[,.\n]*[\s]*', text_rule) if s]
    container = bag_list[0]
    if bag_list[1] == 'contain no other':
        return container, None
    num_bag = re.compile('[0-9]+')
    type_bag = re.compile('(?<=[0-9]\s).+')
    content = {re.search(type_bag, s).group(): int(re.search(num_bag, s).group())
               for s in bag_list[1:]}
    return container, content


dict_rules = dict([extract_rule(rule) for rule in text_rules])


# this counts the root of the tree (shiny gold bag) too
def recursive_count(root: str) -> int:
    content = dict_rules[root]
    if content is None:
        return 1
    else:
        return 1 + sum([recursive_count(bag_type) * bag_number
                        for (bag_type, bag_number) in content.items()])


target_bag = 'shiny gold'

print(recursive_count(target_bag) - 1)
