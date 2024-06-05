k = int(input())
room = list(map(int, input().split()))
# print(room)
total_room = list(set(room))*5

ans = sum(total_room) - sum(room)

ans2 = int(ans/4)
print(ans2)