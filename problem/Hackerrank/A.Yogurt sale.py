t=int(input())
while t>0:
    n=int(input())
    a=int(input())
    b=int(input())
    if(b<a*2):
        print((n//2)*b+(n%2)*a)
    else:
        print(n*a)
    t-=1

    
