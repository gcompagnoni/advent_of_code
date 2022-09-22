import re


def evaluate_expression(expression: str) -> int:
    left_pars = [m.start() for m in re.finditer("[(]", expression)]
    first_right_par = expression.find(')')
    if first_right_par > 0:
        # compute the value of the first bracketed expression we find
        left_par = max([idx for idx in left_pars if idx < first_right_par])  # last '(' before the first ')'
        bracketed_expression = expression[left_par + 1:first_right_par]
        expr_val = evaluate_expression(bracketed_expression)
        new_expression = expression[:left_par] + str(expr_val) + expression[first_right_par + 1:]
        return evaluate_expression(new_expression)
    else:
        return eval_simplified_expression(expression)


def decompose_expression(expression: str) -> tuple[list[str], list[str]]:
    expression = expression.replace(' ', '')
    numbers = re.split("[+*]", expression)
    operators = [c for c in expression if c in ['+', '*']]
    return numbers, operators


def recompose_expression(numbers: list[str], operators: list[str]) -> str:
    expression_list = numbers + operators  # just initialize a list of the right length for slicing
    expression_list[0::2] = numbers
    expression_list[1::2] = operators
    return ''.join(expression_list)


def eval_simplified_expression(expression: str) -> int:
    numbers, operators = decompose_expression(expression)
    if len(numbers) > 1:
        # evaluate the first operation from the left
        first_number = str(eval(numbers[0] + operators[0] + numbers[1]))
        new_numbers = [first_number] + numbers[2:]
        new_operators = operators[1:]
        new_expression = recompose_expression(new_numbers, new_operators)
        return eval_simplified_expression(new_expression)
    else:
        return int(numbers[0])


with open('inputs/input_18.txt', 'r') as infile:
    expressions = infile.read().split('\n')

results=[evaluate_expression(e) for e in expressions]

print(sum(results))
