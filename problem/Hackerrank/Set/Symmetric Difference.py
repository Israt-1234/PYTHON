# Enter your code here. Read input from STDIN. Print output to STD

n = int(input())
m = set(map(int, input().split()))

l = int(input())
k = set(map(int, input().split()))

diff_m = m.difference(k)
diff_k = k.difference(m)
union = sorted(list(diff_m.union(diff_k)))
# print(union)
for i in union:
    print(i)
