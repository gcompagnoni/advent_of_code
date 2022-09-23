from typing import Union


# treat the message as being "consumed" by advancing through a rule
def check_message(msg: str, rule: list[list[int]]) -> bool:
    if rule == [[]] and msg == '':
        return True
    elif len(rule) > 0 and len(msg) > 0:
        # some kind of depth-first search
        for subrule in rule:
            if len(subrule) > 0:
                first_rule = rule_dict[subrule[0]]

                if isinstance(first_rule, str):
                    if first_rule == msg[0]:
                        # consume the first character of the message and go on with evaluation
                        new_subrule = subrule[1:]
                        new_msg = msg[1:]
                        if check_message(new_msg, [new_subrule]):
                            # found a good path!
                            return True
                        else:  # try next subrule
                            continue
                    else:  # try next subrule
                        continue
                else:
                    # rewrite the subrule by "expanding out" the first term
                    new_subrule = [s + subrule[1:] for s in first_rule]
                    if check_message(msg, new_subrule):
                        # found a good path!
                        return True
                    else:  # try next subrule
                        continue

            else:  # try next subrule
                continue

    return False


# only modification to deal with loops is that we need to make sure that
# the non-looping options (there must always be at least one) for a rule come before the looping ones
def reorder_rule(rule_id: int) -> None:
    if isinstance(rule_dict[rule_id], list):
        new_rule = rule_dict[rule_id].copy()
        for subrule in rule_dict[rule_id]:
            if rule_id in subrule:
                new_rule.remove(subrule)
                new_rule.append(subrule)
        rule_dict[rule_id] = new_rule


def rule_as_list(rule_str: str) -> Union[str, list[list[int]]]:
    # assume rules are composed either by other rules or by a single quoted string
    if rule_str.find('"') >= 0:
        return rule_str.strip().replace('"', '')
    else:
        return [[int(x) for x in subrule.strip().split(' ')] for subrule in rule_str.split('|')]


with open('inputs/input_19.txt', 'r') as infile:
    rule_list, messages = [item.split('\n') for item in infile.read().split('\n\n')]

rule_dict = dict(map(lambda x: (int(x[0]), rule_as_list(x[1])), [r.split(':') for r in rule_list]))

# apply modification to specified rules
rule_dict[8] = [[42], [42, 8]]
rule_dict[11] = [[42, 31], [42, 11, 31]]

for idx in rule_dict.keys():
    reorder_rule(idx)

responses = [check_message(msg, [[0]]) for msg in messages]

print(sum(responses))
