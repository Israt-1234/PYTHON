
from itertools import combinations
a, b = input().split()
k = int(b)

for i in range(1, k+1):
    for j in list(combinations(sorted(a), i)):
        print(''.join(j))

