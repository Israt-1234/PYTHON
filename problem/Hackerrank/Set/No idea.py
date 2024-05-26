def solve(n, m, my_array, set_a, set_b):
    happiness = 0
    set_a = set(set_a)
    set_b = set(set_b)
    for i in my_array:
        if i in set_a:
            happiness += 1
        elif i in set_b:
            happiness -= 1
    return happiness

n, m = map(int, input().split())
my_array = list(map(int, input().split()))
set_a = list(map(int, input().split()))
set_b = list(map(int, input().split()))
print(solve(n, m, my_array, set_a, set_b))
