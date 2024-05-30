# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
st = set(map(int, input().split()))
n1 = int(input())
st1 = set(map(int, input().split()))

newst = st.symmetric_difference(st1)
print(len(newst))