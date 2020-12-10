with open('inputs/input_10.txt', 'r') as infile:
    ratings = [int(x) for x in infile.read().split()]

ratings = sorted(ratings)
ratings.append(ratings[-1] + 3)
ratings.insert(0, 0)

# or we could just use numpy...
diff = [ratings[i + 1] - ratings[i] for i in range(len(ratings) - 1)]

num_diff_1 = sum([k == 1 for k in diff])
num_diff_3 = sum([k == 3 for k in diff])

print(num_diff_1 * num_diff_3)
