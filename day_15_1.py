with open('inputs/input_15.txt', 'r') as infile:
    starting_nums = infile.read().split(',')

spoken_nums = {int(num): turn + 1 for turn, num in enumerate(starting_nums)}

turn = len(starting_nums)
cur_num = int(starting_nums[-1])

while turn < 2020:
    turn += 1
    if cur_num in spoken_nums.keys():
        next_num = turn - spoken_nums[cur_num] - 1
    else:
        next_num = 0

    spoken_nums[cur_num] = turn - 1
    cur_num = next_num

print(cur_num)
