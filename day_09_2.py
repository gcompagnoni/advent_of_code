with open('inputs/input_9.txt', 'r') as infile:
    input_lines = infile.readlines()

numbers = [int(x) for x in input_lines]

invalid_pos = 501  # from first part
invalid_num = numbers[invalid_pos]

k = 0
candidate_list = [numbers[k]]
candidate_sum = numbers[k]

# this should require at most 2n additions
# (every number is added and removed from candidates at most once)
while k < invalid_pos:
    while candidate_sum < invalid_num:
        k += 1
        candidate_list.append(numbers[k])
        candidate_sum += numbers[k]
    if candidate_sum == invalid_num:
        print(min(candidate_list) + max(candidate_list))
        break
    remove_value = candidate_list.pop(0)
    candidate_sum -= remove_value
