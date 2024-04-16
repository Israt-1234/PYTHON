friend=["israt","jahan","hello"]    #list
print(type(friend))
print(friend[2])
print(friend[0])

friend.append("world")
print(friend[3])
friend.append("kabir")
print(friend[4])
print(friend)
# friend.remove("kabir")
# friend.pop()
print(friend)
friend.insert(1,"marufa")
print(friend)

print(friend[0:3])
print(friend[:4])           #0 to 4 index print
print(friend[2:])           #2 to last index print
friend.sort()
print(friend)
friend.clear()
print(friend)