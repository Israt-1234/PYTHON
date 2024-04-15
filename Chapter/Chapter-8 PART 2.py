#del keyword- used to delete to object properties or object itself

#del s1.name  or del s1

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("israt")
print(s1.name)

# Now let's not delete the attribute and try to access it
# del s1.name
print(s1.name)

#private(like) attribute and methods

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass    #__acc_pass static 
        
    def reset_pass(self):
        print(self.__acc_pass)


acc1= Account("1234","abcderf")
print(acc1.acc_no)
acc1.reset_pass()

class studen:
    __name="israt"
    name=__name
    def __hello(self):
        print("heelo israt jahan")
    def wecome(self):
        self.__hello()
        self.__name
        
p1 =studen()
print(p1.wecome())
print(p1.name)

#Inheritance

class car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class toyotaCar(car):
    def __init__(self, name):
        self.name=name

car1=toyotaCar("fortuner")
car2=toyotaCar("prius")
print(car1.start())

#multiple inheritance

class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

# super method
#super method are to access parent

# class method- a class method is bound to the class and receives the class as an inplicit first argument

class person:
    name="hello"
    def college_name(self , name):
        person.name=name
       # self.__class__.name="israt"

    @classmethod
    def changename(cls, name):
        cls.name=name

p1= person()
p1.college_name("israt jahan")
print(p1.name)
print(person.name)

p1.changename("jahan")
print(person.name)


#property

class student:
    def __init__(self,phy,chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    @property    #automatoc change
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
st=student(69,67,78)
print(st.percentage)

st.phy=90
print(st.phy)
print(st.percentage)

#Operators and Dunder function
#dunder function is __  
#polymorphism:operator overloading

class complex:
    def __init__(self,real, img):
        self.real=real
        self.img=img

    def numt(self):
        print(self.real,"i +", self.img,"j")

    def add(self, num):
        newReal=self.real+num.real
        newImg=self.img+num.img
        return complex (newReal, newImg)
    # dunder function
    def __add__(self, num):
         newReal=self.real+num.real
         newImg=self.img+num.img
         return complex (newReal, newImg)
    def __sub__(self, num):
        newReal=self.real - num.real
        newImg=self.img - num.img
        return complex (newReal, newImg)

num1=complex(1,3)
num1.numt()

num2= complex(4,6)
num2.numt()

# num3=num1.add(num2)

num3=num1+num2
num3=num1-num2
num3.numt()

