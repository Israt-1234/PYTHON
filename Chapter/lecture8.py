#tuple
#count in tuple
#index in tuple

person_one=("israt", 25 , "dhaka","ctg")
print(person_one)

print(person_one[2])

print(person_one.count("israt"))

print(person_one.index("dhaka"))


#Dictionary 
#print element in dictionary
#print only keys
#print only values
#print both
#update dict


students={
    "israt": 22,
    "rimo": 29,
    "hridoy": 24
}

print(students["israt"])
print(students.keys())
print(students.values())
print(students.items())
students.update({"israt":37, "hello": 98})
print(students.items())
print(students.get("kanir"))