#list in python
"""A built-in type that stores set of values
it can store elements of different types(integer, float,string,etc)"""
marks3=12.23
marks1=90.34
marks2=34.34
marks=[45.45,78.56,12.34,45.23]
print(marks)
print(type(marks))
print(marks[0],marks[1])
student=["takes",55,34,17,"ctg"]
print(student)
student[0]="hello"
print(student)
print(len(student))

# list slicing- similar to string slicing
# list_name[starting_index:ending_index] ending index is not included

marks=[23,34,2,356,78]
print(marks)
print(marks[1:4])
print(marks[-3:-1])

# list methods

list=[2,3,1]
list.append(5)   #add one element at the end 
print(list)      #[2,3,1,5]
print(list.append(6)) #None--append method nehi return hugiya
list.remove(6)         #remove 1st occurance of element-> remove(element)
list.sort()      #sorts in ascending order
print(list)      #[1,2,3,4]
list.sort(reverse=True) #sort in decending order
print(list)      #[5,3,2,1]
list.sort(reverse=False)
print(list)      #[1,2,3,5] 
list.reverse()   #reverse list
print(list)      #[5,3,2,1]

list.insert(2,55) # insert element(index, element)
print(list)

list.pop(2)    #remove element at index here -> pop(index)
print(list)

# python documentation

# Tuples in python-A built-in data type that lets us create immutabe sequences of values

tup=(2,4,1,5,6)
print(type(tup))
print(tup[0])
print(tup[2])
# tup[0]=5  --> value ki change nehi kar cakte -->error ayega
tup=()  #empty tuple
print(tup)
print(type(tup))

tup=(1,) #type->tuple
tup=(1)  #type->int
tup=(2,4,1,5,6)
print(tup[1:3])

# Tuple methods
tup=(2,4,1,5,6)
print(tup.index(1))  #print index
print(tup.count(2))  #count


#WPA to ask the user to enter names of their 3 favorite movies and store them in a list
# a=input("enter the 1st movie: ")
# b=input("enter the 2nd movie: ")
# c=input("enter the 3rd movie: ")

list=[]
list.append(input("enter the 1st movie: "))
list.append(input("enter the 2nd movie: "))
list.append(input("enter the 3rd movie: "))
print(list)

#WAP to check if a list contains a palindrome of elements.

list=[1,3,2,4] #not palindrom
list=[1,2,2,1] #palindrom
pl=list.copy()
list.reverse()
if(pl==list):
    print("palindrom")
else:
    print("not palindrome")

#WPA TO count the number of students with the "A" grade in the following tuple
tup=("C","D","E","A","A","B")
print(tup.count("A"))

#store the above values in a list and sort them from "A" to "D"

list=["B","C","B","D","A"]
print(list.sort())
list.sort()
print(list)