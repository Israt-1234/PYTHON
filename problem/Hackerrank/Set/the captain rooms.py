k = int(input())
room = list(map(int, input().split()))
# print(room)
total_room = list(set(room))*k

ans = sum(total_room) - sum(room)

ans2 = int(ans/(k-1))
print(ans2)