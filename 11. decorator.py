#property decorator working
"""
class Animal:
    @property
    def show(self):
        print("This is a property decorator")
obj = Animal()
obj.show
"""

#decorator working
"""
def decorator(func):
    def wrapper():
        print("will print before function")
        func()
        print("will print after function")
    return wrapper
@decorator
def show():
    print("This is a decorator")
show()
"""

#addtional example of decorator
"""
def decorator(func):
    def wrapper(a,b):
        print("will print before function")
        func(a,b)
        print("will print after function")
    return wrapper
@decorator
def add(a,b):
    print("The sum is ",a+b)
add(5,10)
"""

#if we want to pass some arguments in the function then we can use *args and **kwargs in the wrapper function

#args 
"""
def add (a,b):
    print("The sum is ",a+b)
add (1,2,3,4) #this will give an error because add function is only accepting 2 arguments but we are passing 4 arguments
"""
"""
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print("The sum is ",sum)
add(1,2,3,4) #this will work because we are using *args in the function
"""
#kwargs
"""
def info(**kwargs):
    print("ur info is: \n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")
info(name="John",age=30,city="New York") #this will work because we are using **kwargs in the function
"""
#if we want to pass some arguments in the function then we can use *args and **kwargs in the wrapper function
"""
def decorate(func):
    def wrapper(*args,**kwargs):
        print("will print before function")
        func(*args,**kwargs)
        print("will print after function")
    return wrapper
@decorate
def add(a,b,c):
    print("The sum is ",a+b+c)
add(5,10,67) 
"""