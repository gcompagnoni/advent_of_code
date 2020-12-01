with open('input_1_1.txt', 'r') as infile:
    s = [int(x) for x in infile.readlines()]

s.sort()
global_sum = 2020


def recursive_binary_search(r, x, my_sum):
    if len(r) == 0:
        return None
    y_index = len(r) // 2
    y = r[y_index]
    if x + y == my_sum:
        return y
    elif x + y < my_sum:
        return recursive_binary_search(r[y_index + 1:], x, my_sum)
    elif x + y > my_sum:
        return recursive_binary_search(r[:y_index], x, my_sum)


for j, z in enumerate(s):
    target_sum = global_sum - z
    for k, x in enumerate(s[j + 1:]):
        y = recursive_binary_search(s[k + 1:], x, target_sum)
        if y is not None:
            break
    if y is not None:
        print(z, x, y, z * x * y)
        break
