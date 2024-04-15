"""comments in python"""
#single line comment -->understanding redability
"""multiple line comment""" 
# python is case sensitive
#Data type:
#*Integers   +ve,-ve,0 (-24,24,0)
#*String     "hello israt"   -' ',""   name="sk" name='sk' name='''name'
  
#*Float       3.22

#*Boolean     True False
#*None        a=None 

age =23
old=True
a=None
print(type(old))
print(type(a))


#keywords
#keywords re reserved words in python
 
#google follow --else if in is finally ect

#print sum,diff, product

a=2
b=4
sum=a+b
print(sum)

#types of Tokens-punctuators are symbole to organie structure in programming 
#(),{},@,[],# etc
#python is typed language
#typed means-implicity(py) and explicity(c++,java)


#expression execution--
#string ans numeric values can operate together with*

A,B=2,3
text="@"
print(2*text*3)          #@@@@@@

A="2"
print((A+text)*B)        #2@2@2@
#ATITHMETIC OPERATORS

#ARITHMETIC EXPRESSION WITH INTERGER AND FLOAT WILL RESULT IN FLOAT

a,b=10,5
C=a*b
print(C)   #50.0

#expresssion execution
#RESULT OF DIVTION OPERATOR WITH two integers will be float
a,b=2,3
c=a/b
print(c)  #0.666666

#integer division with float and int will give intdisplayed as float
a,b=1.5,3
c=a//b    #0.0 (int)
c=a/b      #0.5 (float)

#floor gives closest interger, which is lesser than or euqal to the float value result of (A//B)is same as floor (A/B)
#floor(number)->closect int---4.99-4,5.5-5

A,B=12,5
C=A//B   
print(C)      #2

B=-2
C=A//B        #-3   
#ceil
A,B=12,5
C=A//B+1  
print("ceil",C)      #3

#remainder is negative when denominotor is negative

A,B=-5,2
c=A%B
print(c)      #1


A,B=5,2
c=A%B
print(c)      #1

A,B=5,-2
c=A%B
print(c)      #-1

A,B=-5,-2
c=A%B
print("heloo",c)      #1

#print("hello")--wont be printed
print("world")    #will be printed

#input in python

#input() statement is used to accept values (using keybord)from user

name=input("nm: ")               #string input
age = int(input("age : "))       # int input
price =float(input("price : "))  #float input

print("my nme is ", name, "i am ", age, "years old")

#a^b   --->a**b
print(2**3)   #8


#conditional statement------>>
#if-elif-else
"""
if(condition):
  statement
elif:
   statement
else:
    statement
"""
#light color
light=input("light: ")
if (light=="red"):
    print("stop")
elif(light=="yellow"): 
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")
  

#grades of students
marks=int(input("marks : "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("c")
else:
    print("fail")   


##
A=int(input("A :"))
G=input("m/f :")
if((A==1 or A==2 )and G=="M"):
    print("free is 100")
elif A == 3 or A == 4 or G == "F":
    print("free is 200")
elif(A==5 and G=="M"):
    print("free is 300")
else:
    print("no free")


#Single line if/Ternary operator
    
#<var>=<var1>if<condition>else<var2>

food=input("food : ")
eat ="yes" if food =="cake" else "NO"
print(eat)

#<stt1> if<condition> else<stt2>

food=input("food: ")
print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")

#Clever if/Ternary Operator
#<var>=(false_val,true_val)[<condition>]

age=int(input("age: "))
vote=("yes", "no")[age>=18]

salary=float(input("salary : "))
tax=salary*(0.1,0.2)[salary>5000]
print(tax)

#best practice in python
#type of operator
#arithmatic operator
a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

#relational operator
a=50
b=20
print(a==b) #false   boolean value
print(a!=b) #true
print(a>=b) #true
print(a<b)  #false

#assignment operator
num=20
num=num+10 #30
num+=10
print(num)  #40
#*-/ ** %

#logical operator
print(not True)  #false
print(not False) #true

a=50
b=30
print(not False)
print(not (a>b))


val=True
val1=False
print("and operator ",val1 and val) #false
print("or operator ",val1 or val) #true
print("or operator ",(a==b) or (a>b)) #ftrue

#type conversion
#python automatically int to float convert karta he
a=2
b=4.24
sum= a+b 

#type casting
a.b=1,"2"
c=int(b)
sum=a+c
d=str(c)

#input in python
val=input("enter your name : ")
print(type(val), val)

#write a program to input 2 numbers and print their sum

num1=int(input("enter 1st num: "))
num2=int(input("enter second : "))
print("sum = ",num1+num2)

#print area
#input 2 floating number and their avg
#input 2 number print true is a is grater than or equal to b.if not print false

print(num1>=num2)  #23 , 4 -->true





