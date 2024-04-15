#file i/0 in python
# Type of all file
# 1.text file: txt,docx,log ect
# binary file:mp4,mov,png,jpeg ect

#open read and close
#text must be another file 
f = open("demo.txt", "r")
print(f.readable())  # Corrected to f.readable() to call the attribute
data = f.read()
print(data)
print(type(data))
f.close()

# reading a file
"""data=f.read()  #read entire file
data =f.readline() #reads one line at a time
"""
f = open("demo.txt", "r")
line1=f.readline()
print(line1)

line2=f.readline()
print(line2)


#writing to a file

f=open("demo.txt","w")
f=f.write("hey this is israt jahan")  #overright the entire file
# print(f)  #total char

f=open("demo.txt","a")
data=f.write("\nthis is a new line")    #adds to the line
# print(data)
f.close()

f=open("simple.txt","w")
f.close()
f=open("simple.txt","a")
f.close()
f=open("simple.txt","r+") #point start -no trancate
f.read()  #reading and(overright) writing
f.write()
f.close()
f=open("simple.txt","w+")#reading and(overright) writing - trancate
f.read() 
f=open("simple.txt","a+") #reading and(overright) writing point end->no trancate
f.read() 

#with Syntax
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","r") as f:
    data = f.write("new data")

#delationg file
import os
os.remove("simple.txt")

with open("practice.txt","w") as f:
    f.write("hi everyone\nwe are larning file i/o")
    f.write("\nusing java")


with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)

word="hello"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("NOTfound")



