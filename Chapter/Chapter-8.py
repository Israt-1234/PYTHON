#OOP in python- to map with real world scenarions,using object in code
# class and object in python- class is a blueprint for creating objects

class Student:
    name="israt"
#create object
s1=Student()
print(s1.name)
s2=Student()
print(s2.name)

class car:
    colo="blue"
    brand="marcedes"
cr=car()
print(cr.colo)
print(cr.brand)


#__init__ function(constructor)
#self parameter is a reference to the current instance of the class and use to access variables that belongs to the class
class student :
    #  def __init__(self):
    #       pass     #default constructor
         
    def __init__(self,fullname,markes):     #init function -constructor--parameterized
        self.name=fullname
        self.markes=markes   #object attribute
        print("hello israt jahan")
    college_name="ABC College"
    markes="annnonimas"    #class attribute

    #method
    def welcome(self):
        print("hello welcome")
        print("hi", self.name)
    def get_marke(self):
        return self.markes

s1=student("Raiyan",97)
print(s1.name, s1.markes)  #raiyan 97
# print(s1.markes)
print(s1.college_name)
print(student.college_name)
print(student.markes)
print(s1.markes)

s1.welcome()
print(s1.get_marke())
#class and instance attributes

#create student class that takes name and marks of 3 subjects as arguments in constructor
#then create a method to print the average

class student():
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def Average(self):
        sum=self.marks3+self.marks1+self.marks2
        Avg=sum/3
        print(Avg)

s=student("Raiyan",30,40,30)
s.Average()

class mar():
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def get_Avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"your avg marks is:",sum/3)

    #static method 
    @staticmethod
    def hello():
        print("hey hello")
    
s1 = mar("tony stark", [89,45,45])
s1.get_Avg()

s1.name=("ironman")
s1.get_Avg()
s1.hello()    # hey hello

#4 pillar of oop 
#Abstructor -- hiding the implementation details of a class and only showing the essintial features to the user

#Encapsultaion->wrapping data and functionn into a single unit(object)

"""create account class with 2 attributes balance and account no
create methods for debit, credit and printing the balance
"""

            
class Account:
    def __init__ (self, bal, aCC):
        self.balance=bal
        self.aCC=aCC
    #debit method
    def debit(self, amount):
        self.balance-=amount
        print("bd.",amount,"was debited ")
        print("total balance= ",self.get_balance())

    def credit(self, amount):
        self.balance+=amount
        print("bd.",amount,"was credited ")
        print("total balance= ",self.get_balance())
    
    def get_balance(self):
        return self.balance


acc1= Account(10000,12345)
print(acc1.balance, acc1.aCC)
acc1.debit(1000)
acc1.credit(500)