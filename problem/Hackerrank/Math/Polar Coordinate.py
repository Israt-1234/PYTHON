import cmath
def polar(z):
    r = abs(z)
    p =cmath.phase(z)
    return r, p;

z = complex(input().strip())
x,y=polar(z)

print(x)
print(y)


