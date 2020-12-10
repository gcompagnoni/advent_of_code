from functools import lru_cache

import numpy as np

with open('inputs/input_10.txt', 'r') as infile:
    ratings = [int(x) for x in infile.read().split()]

ratings = sorted(ratings)
ratings.append(ratings[-1] + 3)
ratings.insert(0, 0)
ratings = np.array(ratings)

diff = np.diff(ratings)


# Now note that if ratings[i + 1] - ratings[i] = 3, then both ratings[i] and ratings[i+1] must
# belong to every valid chain. Since there are no two neighbours with a difference of two,
# the problem can be reduced to counting how many valid chain can be created from a block of
# n consecutive numbers.
# This obeys a simple recurrence relation: N(k)=N(k-1)+N(k-2)+N(k-3)

@lru_cache()
def num_chains(len_1s: int) -> int:
    if len_1s < 0:
        return 0
    elif len_1s == 0:
        return 1
    else:
        return num_chains(len_1s - 1) + num_chains(len_1s - 2) + num_chains(len_1s - 3)


pos_3s = np.where(diff == 3)[0]
# we know the last element is a 3, so we do not need a dummy at the end
diff_pos_3s = np.diff(np.insert(pos_3s, 0, -1))
len_block_1s = diff_pos_3s[diff_pos_3s > 1] - 1

num_chains_block = np.array([num_chains(n) for n in len_block_1s])
num_all_chains = np.prod(num_chains_block)

print(num_all_chains)
