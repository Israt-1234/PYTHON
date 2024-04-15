# Dictionary in python
# Dictionary are used to store data values in key:value pairs
# they are unordered, mutable(changeable) & dont allow duplicate keys

info={
    "key":"value",
    "name":"hello israt",
    "learning": "coding",
    "age":35,
    "is_adult":True,
    "marks":94.4,
    "subject":["python","c","c++"],
     "topics":("dict","set"),
      12.34:234.45,

}
print(info)
print(type(info))

# dict["key"]="value"
print(info["age"])
print(info["key"])

info["key"]="israt"  #overwrite
print(info["key"])

null_dict={}
print(null_dict)
null_dict["name"]="hello"

# Nasted Dictionaries
student={
    "name":"israt",
    "subject":{
        "phy":45,
        "chem":40,
        "math":90
    }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"])
#method of dictionary
#mydict.keys()           #return all keys
#mtdic.values()          #return all values
#mydic.items()           #return all (key, val) pairs as tuples
#mydic.get("key")        #return the according the value
#mydic.update(newDict)   #insert the speccified items to the dictonary
print(student.keys())
print(len(student))
#type cust
print(list(student.keys()))
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())  #---> tuple return  in items
pairs=list(student.items())
print(pairs[1])

print(student["name"])    
print(student.get("name")) 

stu=({"city": "halishahar", "age":89})
student.update(stu)
print(student)

#Set in python
"""set is the collection of the unordered items
each element in the set must be unique and immutable"""
#list and dict add nehi huty cz they are mutable

collection={1,2,3,4,"hello","hello","world"}
print(collection)
print(type(collection))
print(len(collection))

collection={} #empty dictonary
collection=set() #empty set

# set method
"""set.add(el)    #adds an element
set.remove(el) #removes the element
set.clear()    #empties the set
set.pop()      #removes a random value"""

collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1)
collection.add("hello")
collection.add("israt")
collection.add((1,2,3))
print(collection)
print(len(collection))
collection.clear()
print(len(collection))

collection={"helo","israt","college","python"}
print(collection.pop())
print(collection)

#Set Methods
# set.union(set2)  #combain both set values and returns new
# set.intersection(set2) #combain common values and return new

Set1={1,2,3,4,5}
Set2={2,4,5,6,7,8}
print(Set1.union(Set2))
print(Set1.intersection(Set2))

#practice

#store following word meanings in a python dictionary:

dic={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"

}
print(dic)
print(type(dic["table"]))

#you are given a list of subjects for students.Assume one classroom is required for 1 subject.how many classrooms are needed by all students
sets={"python","java","c++","c","javascript","python","java","c++","c"}
print(len(sets))

#WAP to enter marks of 3 subjects from the user and sore them is a dictionary.start with ana empty dictionary and add one by one .use subject name as key and marks as value

dic={}

x=int(input("enter phy: "))
 
dic.update({"phy":x})
x=int(input("enter the che : "))
dic.update({"che":x })
x=int(input("enter the bio: "))
dic.update({"bio":x})
print(dic)

#figure out a way to store 9 and 9.0 as separate values in the set

set1= set()
set1.add(9)
set1.add("9.0")
print(set1)

