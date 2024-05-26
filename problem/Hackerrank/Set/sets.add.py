# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
st = set()
for i in range(n):
    s = input()
    st.add(s)
    count = len(st)
print(count)


