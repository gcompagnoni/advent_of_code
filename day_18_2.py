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


def decompose_expression(expression: str) -> tuple[list[int], list[str]]:
    expression = expression.replace(' ', '')
    numbers = [int(x) for x in re.split("[+*]", expression)]
    operators = [c for c in expression if c in ['+', '*']]
    return numbers, operators


def recompose_expression(numbers: list[int], operators: list[str]) -> str:
    expression_list = numbers + operators  # just initialize a list of the right length for slicing
    expression_list[0::2] = [str(n) for n in numbers]
    expression_list[1::2] = operators
    return ''.join(expression_list)


# only changed function compared to part 1
def eval_simplified_expression(expression: str) -> int:
    numbers, operators = decompose_expression(expression)

    if expression.find('+') > 0:
        # evaluate the first addition operation from the left
        idx = operators.index('+')
        # i-th operator sums i-th and (i+1)-th numbers
        s = numbers[idx] + numbers[idx + 1]
        new_operators = operators[:idx] + operators[idx + 1:]
        new_numbers = numbers[:idx] + [s] + numbers[idx + 2:]
        new_expression = recompose_expression(new_numbers, new_operators)
        return eval_simplified_expression(new_expression)
    else:
        # there are only multiplications, so it is the same as usual arithmetic
        return eval(expression)


with open('inputs/input_18.txt', 'r') as infile:
    expressions = infile.read().split('\n')

results = [evaluate_expression(e) for e in expressions]

print(sum(results))
