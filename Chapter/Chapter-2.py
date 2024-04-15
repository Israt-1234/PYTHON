#strings
#string is data type that store a sequence of characters

"""basic of operation--
*concatenation --> "hello"+"world"="helloworld"
*length of str  --> len(str)"""

str1="this is string.\ni am python"    #next line--> \n
str11="this is string.\ti am python"   #space-tab    --> \t
str2='this is string 2'
str3="""this is a string 3"""

print(str1)
print(str11)
print(str2+" "+str3)
print(len(str2))

#indexing-position
"""I s r a t J a h a n
   1 2 3 4 5 6 7 8 9 10"""
ch=str1[1]
print(ch)
print(str1[1])

#string slicing-Accessing parts of a string
#str[starting_idx:ending_idx]  #ending index is not included
# str="hello israt"
# str[1:4] is'ell'

print(str1[0:4])
print(str2[6:len(str2)])
print(str2[5:]) #[5:len(str2)]
print(str2[:4]) #[0:4]

#negative index
"""i  s  r  a  t
  -5 -4 -3 -2  -1"""

str="Orange"
print(str[-3:-1])  #ng  # ending index(-1) is not included

#string Functions
str ="hello this is israt jahan"
print(str.endswith("jahan"))  #last substr is jahan so ans will be return boolean True
print(str.endswith("istat"))  #False
print(str.capitalize())       #Capitalise first char
str1=str.replace('o',"a")     #replace all occurance of old value to new value
print(str1)
print(str1.find("is"))        #return 1st index of 1st occurance
print(str1.count("i"))        #count the accurance of substring
print(str1.count("israt"))

#input user first name and print its length

str="israt"
print(len(str))


"""condition statements--->>
if-elif-else(SYNTAX)"""
    
"""
if(condition):
    statement1
elif(condition):
    statement2
else
    statement3"""
#solve trafic light code using if else condition
age =33
if(age>=18):
    print("you are adult")
    print("you can apply")
else:
    print("you are disqulafied")
print("end of code")

#this statement convert code
#Grade students based on marks
"""marks>=90,grade="A"
90>marks>=80, grade="B"
80>marks>=70, grade="C"
70>marks,grade="D"""

#nesting loop

age=90
if(age>=56):
    if(age>=78):
        print("you can not apply")
    else:
        print("you can apply")
else:
    print("cannot drive")

#wap to check if a number entered by the user is odd or even
#find the greatest of 3 numbers entered by the user

a=int(input("enter the first number: "))    
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))

if(a>=b and a>=c):
    print("a is greatest ",a)
elif(a<b and b>=c):
    print("b is greatest ",b)
else:
    print("c is gratest ",c)
#to check if a number is multiple of 7 or not
