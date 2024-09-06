from itertools import permutations
s, k = input().split()

for item in sorted(list(permutations(s, int(k)))):
    print(''.join(item))

