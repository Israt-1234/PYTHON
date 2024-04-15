#function in python-> block of statements that perform a specific task

"""def fun_name(param1,param2...):"""
def clsum(a, b):
    sum=a+b
    print(sum)
   # return sum
clsum(3,4)   #function call:arguments

def cal_sum(b,c):
    return b*c
print(cal_sum(3,4))

def print_hello():
    print("hello")
print_hello()
print_hello()
output=print_hello()
print(output)  #none cz no return 

# 2 funtion --> built-in function ,user define function

print("hel srat",end=" ")  #sep=" "
print("jahn")       #end="\n"

#default param

def cal_sum(a=1,b=2):   # i dont use a=1 and b=2 then its error a jaye ga
    print(a*b)
    return a*b
cal_sum()

def cal_sum(a,b=2):   # i dont use a=1 and b=2 then its error a jaye ga
    print(a*b)
    return a*b
cal_sum(1)

#WAP to print the length of list(list is the parameter)
#WAP to print the elements of a list in a single line(list is the parameter)

def list_len(list):
    length=len(list)
    return length
def print_list(list):
    for i in list:
        print(i,end=" ")

list=[2,3,4,5,5,6,7]
li=list_len(list)
print(li)

print_list(list)
print()

#WAf to find the factorial of n .(n is the parameter)

def fact(a):
    factorial=1
    for i in range(1, a+1):
        factorial*=i
    return factorial
print(fact(5))

#WAP TO CONVERT USD TO INR

def convert(usd_vl):
    inr_vl=usd_vl*83
    print(usd_vl,"usd =", inr_vl,"inr")
convert(3)

# Recursion -> when a function cblles iteself repeatedly

def show(n):
    if(n==0):
        return 
    print(n,end=" ")
    show(n-1)

show(3)
print()
#return n!

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(4))

#WA RECURSIVE FUNCTION TO CALCULTATE THE SUM OF FIRST N NATURAL NUMBER

def sum_n(n):
    if(n==0): 
        return 0
    else:
        return n+sum_n(n-1)

print(sum_n(10))

#wa recursive function to print all elements in s list(use list & index as parameters)

def list_ind(list, ind=0):
    if(ind==len(list)):
        return
    print(list[ind],end=" ")
    list_ind(list, ind+1)

list=[3,4,5,6,7,8]

ans=list_ind(list)
