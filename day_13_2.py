from typing import Tuple

import numpy as np

with open('inputs/input_13.txt', 'r') as infile:
    ids = infile.read().split()[1]

remainders = {int(k): (i % int(k)) for (i, k) in enumerate(ids.split(',')) if k.isdigit()}

for m in remainders.keys():
    for n in remainders.keys():
        if m != n:
            if np.gcd(m, n) > 1:
                print(f'gcd({m},{n}) = {np.gcd(m, n)}')
                break


# Since all divisors are pair-wise coprime, the Chinese Remainder Theorem guarantees the existence
# of a solution smaller than their product.

# We compute using this method
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(direct_construction)

# from https://codegolf.stackexchange.com/questions/69582/b%c3%a9zouts-identity
def bezout(a: int, b: int) -> Tuple[int, int]:
    r = b
    x = a  # becomes gcd(a, b)
    s = 0
    y = 1  # the coefficient of a
    t = 1
    z = 0  # the coefficient of b
    while r:
        q = x // r
        x, r = r, x % r
        y, s = s, y - q * s
        z, t = t, z - q * t
    return y % (b // x), z % (-a // x)


bezout_v = np.vectorize(bezout, otypes=[np.int64, np.int64])

divisors = np.array(list(remainders.keys()), dtype=np.int64)
remainders = (-np.array(list(remainders.values()), dtype=np.int64)) % divisors
P = divisors.prod()
N = P // divisors
M = bezout_v(N, divisors)[0]
s = ((M * N * remainders) % P).astype(np.int64).sum()

print(int(s % P))
