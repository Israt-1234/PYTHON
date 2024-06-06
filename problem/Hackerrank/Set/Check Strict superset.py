

set_a = set(map(int, input().split()))
n = int(input())
check = True
for i in range(0, n):
    set_b  =set(map(int, input().split()))
    for i in set_b:
        if i in set_a:
            continue
        else:
            check = False
    if(check == False):
        break
print(check)

            
