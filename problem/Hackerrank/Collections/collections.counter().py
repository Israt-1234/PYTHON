# Enter your code here. Read input from STDIN. Print output to STDOUT`
from collections import Counter
n = int(input())
sotck = list(map(int, input().split(' ')))
# print(sotck)
dict = Counter(sotck)

k = int(input())
p = 0
for i in range(k):
    size, price = map(int, (input().split(' ')))
    if dict[size]:
        dict[size]-=1
        p = p + price
print(p)


