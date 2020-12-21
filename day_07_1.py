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


def recursive_search(bag: str, target: str) -> bool:
    content = dict_rules[bag]
    if content is None:
        return False
    elif target in content.keys():
        return True
    else:
        return any([recursive_search(b, target) for b in content.keys()])


target_bag = 'shiny gold'

allowed_containers = [bag for bag in dict_rules.keys() if recursive_search(bag, target_bag)]

print(len(allowed_containers))
