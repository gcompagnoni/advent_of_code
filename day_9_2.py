with open('inputs/input_9.txt', 'r') as infile:
    input_lines = infile.readlines()

numbers = [int(x) for x in input_lines]

invalid_pos = 501  # from first part
invalid_num = numbers[invalid_pos]

k = 0
candidate_list = [numbers[k]]

while k < invalid_pos:
    while sum(candidate_list) < invalid_num:
        k += 1
        candidate_list.append(numbers[k])
    if sum(candidate_list) == invalid_num:
        print(min(candidate_list) + max(candidate_list))
        break
    candidate_list.pop(0)
