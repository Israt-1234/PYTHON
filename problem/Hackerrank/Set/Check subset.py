# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
while a > 0:
    a = a-1
    n = int(input())
    li = set(map(int, input().split()))
    n1 = int(input())
    li1 = set(map(int, input().split()))
    # if(len(li - li1)==0):
    #     print("True")
    # else:
    #     print("False")
    print(li.issubset(li1))
