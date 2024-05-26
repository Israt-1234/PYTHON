n = int(input())
st = set(map(int, input().split()))
ty = int(input())
for i in range(ty):
    command = input().split()
    if(command[0] == "pop"):
        st.pop()
    elif(command[0]=="remove"):
        st.remove(int(command[1]))
    elif(command[0] == "discard"):
        st.discard(int(command[1]))
print(sum(st))