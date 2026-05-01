#imperative approach
"""
a = 12
b = 13
print(a + b)
"""

#functional approach
"""
def add(x, y):
    return x + y
print(add(12, 13))
print(add(5, 7))
"""

#object oriented approach
"""
class Factory:
    a = 12

    def hello():
        print("hello world")

    print("this is factory")

print(Factory.a)
Factory.hello()
"""

#object creation
"""
class Factory:
    a = 12

    def hello(self):
        print("hello world")
        
    print("this is factory")

obj = Factory()
print(obj.a)
obj.hello()
"""

#constructor
"""
class Car:
    def __init__(self, company, color, speed):
        print(self) #this will print the address of the object created
        self.company = company
        self.color = color
        self.speed = speed
        
    def show(self):
        print(f" your car have this feature: {self.company}, {self.color}, {self.speed}")

bmw = Car("BMW", "red", 348)
porshe = Car("Porshe", "black", 400)
print(bmw.company, bmw.color, bmw.speed)
print(porshe.company, porshe.color, porshe.speed)

bmw.show()
porshe.show()
"""
#types of attributes
"""
#class attribute and instance attribute 
class Factory:
    a = 12 #class attribute

    def __init__(self, name):
        self.name = name #instance attribute
"""
#types of methods
"""
#instance method, class method and static method

class Animal:
    name = "lion" #class attribute
    def __init__(self, age):
        self.age = age #instance attribute
    def show(self):
        print(f"this is {self.name} and its age is {self.age}") #instance method
    @classmethod
    def hello(cls):
        print(f"hello this is {cls.name}") #class method
    @staticmethod
    def welcome():
        print("welcome to the world of python") #static method

#myself

 class Animal:
    name = "lion" #class attribute
    def __init__(self, age):
        self.age = age
    def show(self):
        print("Hi")
    @classmethod
    def hello(cls):
        print("this is class method")
    @staticmethod
    def static():
        print("this is static method")

obj = Animal(5)
obj.show()
Animal.hello()
Animal.static()       
"""

#inheritance
"""
class Factory:
    a = "i am an attribute of Factory class"
    def hello(self):
        print("i am a method of Factory class")
class Factory2(Factory):
    pass
obj = Factory()
print(obj.a)

obj2 = Factory2()
obj2.hello()
"""
#constructor in inheritance
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"this is your name : {self.name}")
class Human(Animal):
    pass
obj1 = Human("deep")
obj1.show()
"""
#constructor in inheritance with super()
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"this is your name : {self.name}")
class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def show(self):
        print(f"this is your name : {self.name} and your age is {self.age}")

obj2 = Animal("lion")
obj2.show()

obj1 = Human("deep", 22)
obj1.show()
"""
#multiple inheritance
"""
class Animal:
    name1 = "lion"
class Human:
    name2 = "deep"
class Robot(Animal, Human):
    name3 = "robo"
obj = Robot()  
print(obj.name1)
"""
"""
class Animal:
    def __init__(self, name):
        pass
class Human:
    def __init__(self, name, age):
        pass
class Robot(Animal, Human):
    name = "robo"
obj = Robot()
print(obj.name)
"""

#multile inheritance with super()
"""
class Factory:
    def __init__(self, materials, zips):
        self.materials = materials
        self.zips = zips
class Factory2:
    def __init__(self, materials, zips, color):
        super().__init__(materials, zips)
        self.color = color
class Factory3(self, materials, zips, color, pockets):
    def __init__(self, materials, zips, color, pockets):
        super().__init__(materials, zips, color)
        self.pockets = pockets
"""

#polymorphism

"""
def show():
    print("this is a function")
def show():
    print("this is another function")
show()
"""
#method overriding
"""
class Animal:
    def show(self):
        print("hi")
class Human:
    def show(self):
        print("hello")
obj = Human()
obj.show()
"""
#duck typing
"""
class Animal():
    def show(self):
        print("this is an animal")
class Human():
    def show(self):
        print("this is a human")
obj1 = Animal()
obj2 = Human()
obj1.show()
obj2.show()
"""

#encapsulation
"""
#access modifiers 3 types
#public, private and protected

#public
class Factory:
    a = "pune"
    def show(self):
        print("this is a factory")
class Bhopal(Factory):
    def show2(self):
        print(super().a)
obj = Bhopal()
obj.show2()

#private
class Factory:
    _a = "pune"
    def _show(self):
        print("this is a factory")
class Bhopal(Factory):
    def show2(self):
        print(super()._a)
obj = Bhopal()
obj.show2()

#protected
class Factory:
    __a = "pune"
    def __show(self):
        print("this is a factory")
obj = Factory()
print(obj.a)
print(obj.__a)
"""

#abstraction
"""
from abc import ABC, abstractmethod
class Abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
"""

#dundar methods
"""
#normal one
class Animal():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"this is {self.name}"
obj = Animal("lion")
print(obj)

#__add__

class Animal():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"this is {self.name}"
    def __add__(self, other):
        return f"your sum of ages are {self.name + other.name}"
obj1 = Animal("lion",5)
obj2 = Animal("tiger", 7)
print(obj1 + obj2)

#if there are 3 things to add

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"this is {self.name}"
    
    def __add__(self, other):
            sum = 0
            for i in other:
                sum = sum + i.age
            return f"your sum of ages are {self.age + sum}"
obj1 = Animal("lion",5)
obj2 = Animal("tiger", 7)
obj3 = Animal("leopard", 8)
print(obj1 + (obj2, obj3))
"""
