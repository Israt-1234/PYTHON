#loops in python
# loops are used to repeat instructions
"""while condition:
    some work"""

count=1
while count <= 5:
    print("hello")
    count+=1
print(count)

i=1
while (i<=10):
    print("israt", i)
    i+=1
print(i)

#print number from 1 to 5

i=1
while(i<6):
    print(i)
    i+=1
print("end code")

i=5
while i>=1:
    print(i)
    i-=1
print("code ended")

#print the multification table of a number n

n=3
i=1
while i<=10:
    print(n*i)
    i=i+1
print("ended code")

#print the element of following list

num=[2,3,1,5,6,7,90]
heros=["hello","jahan","hey","israt","superman","batman"]
# print(num[0])
i=0
while i<len(num):
    print(num[i])
    i+=1

print("end loop")


i=0
while (i<len(heros)):
    print(heros[i])
    i+=1
print("end loop")

#search for a number x in this tuple using loop

num=(2,3,1,5,6,7,90)
x=7
i=0
while i<len(num):
    if(num[i]==x):
        print("found at index",i)
    else:
        print("not found")
    i+=1
print("code is ended")


#Break and continue

i=1
while i<5:
    print(i)
    i+=1
    if(i==3):
        break
print("end of looop")

# loops in python

# loops are used for sequential traversal.for traversing list, string ,tuples ect

list=[1,2,3,4]
for el in list:
    print(el)
print("end list ")
tup=(3,3,4,5,6,7,8)
for el in tup:
    print(el)
print("end")

str="helloisrtjhn"

for ch in str:
    print(ch)
print("endl")

#print the elements of the following list using  loop

list=[1,4,9,6,36,64,8,100]

for el in list:
    print(el)
print("end this code")

#search for a number x in this tuple using loop

tup=(1,4,5,6,36,64,8,00)
x=6
ind=0
for el in tup:
    if(el==x):
     print("element is found",ind)
     break
    ind+=1


#range()->range functions returns a sequence of numbers, starting from 0 by default and increments by s (by default),and stops before a specified number
"""range(start?, stop,step?)"""
print(range(5))  #(0,5)
for i in range(5):
    print(i)

for i in range(2,10):  #range(stat,stop)
    print(i)

for i in range(2,10,2):  #range(stat,stop,step)
    print(i)

for i in range(2,102,4):
    print(i)


#print number 1 to 100
#print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#print the multification table of n

a=2
for i in range(1,11):
    print(i*a)

#pass statement->pass is null statement that does nothing.it is used as a placeholder for future code

for el in range(10):
    pass

print("some useful work")

#WAP  TO FIND THE SUM OF FIRST N NUMBERS(USING WHILE)

n=10
sum=0
i=1
while i<=n:
    sum+=i
    i+=1

# for i in range(n+1):
#     sum+= i
#     i+=1
print(sum)

n=10
fact=1

for i in range(1, n+1):
    fact*=i
print(fact)
 
