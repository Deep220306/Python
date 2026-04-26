\
# this is comment
"""This 
is
multi line comment"""
"""variables"""
# hulu = "this is a variable" 
# SheryiansSchool = "students" #pascal case
# sheryiansSchool = "students" #camel case
# sheryians_school = "students" #snake case

#--------------
"""
a = 3
b = 4.5
c = "this is a string"
d = 34j
e = True
print(type(a), type(b), type(c), type(d), type(e))
print(ord("a")) # to get the unicode of a character
print(chr(97)) # to get the character from unicode
print(c[0]) # to get the first character of the string
print(c[3:7]) # to get a substring from index 3 to 6
print(c[2: : 1]) # to get every character from index 2 to the end
print(c[ : : -1]) # to reverse the string 

"""

#---------type conversion
"""
a=5500
a=str(a)
print(a)
print(type(a)) 
"""

#---------input output and formatted string
"""
name = input("enter your name: ")
age = int(input("enter your age: "))
print("your name is " + name + " and your age is " + str(age))
print(f"your name is {name} and your age is {age}") #formatted string   
"""
#compound assignment operator
"""
a = 5
a += 3 # a = a + 3
print(a)
"""

#comparison operator
"""
a = 5
b = 3   
print(a > b) # true
print(a < b) # false
print(a == b) # false
print(a != b) # true    
print(a >= b) # true
print(a <= b) # false   
print(a > 3 and b < 5) # true
print(a > 3 or b < 5) # true    
print(ord("a") > ord("b")) # false
""" 
#-----------logical operator
"""
print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)
print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)
print(not 12 == 12)
"""

#------------conditional statement
"""
age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
"""

# else-if statement
"""
money = int(input("please provide me the money :- "))

if money == 10:
    print("I will have a choco bar icecream")

elif money == 20:
    print("I will have a mangodolly")

elif money == 30:
    print("I will have a frosty")
    
else:
    print("I will have a cone")
"""

#Accept 2 numbers and print the greatest number between them
"""
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both the numbers are same")
"""

# Accept the gender from the user as character and print the respective messege
"""
gen = input("please tell your gender as character (M or F):-")

if gen == 'M' or gen == 'm':
    print("Good morning SIR")
elif gen == "F" or gen == 'f':
    print("Good morning MAM")
else:
    print("Unidentified gender")
"""

# accept an intger and print whether it is even or odd
"""
num = int(input("enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:    
    print(f"{num} is an odd number")   
"""

#accept namer and age from the user and check whether the person is eligible for voting or not
"""
name = input("enter your name: ")
age = int(input("enter your age: "))        
if age >= 18:
    print(f"{name} you are eligible to vote")
else:
    print(f"{name} you are not eligible to vote")   
"""

#accept the year and check whether it is a leap year or not
""" 
year = int(input("enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year") 
else:
    print(f"{year} is not a leap year")
"""

#if-elif-else ladder
"""
marks = int(input("enter your marks: "))
if marks >= 90:
    print("you got A grade")
elif marks >= 80:
    print("you got B grade")
elif marks >= 70:
    print("you got C grade")
elif marks >= 60:
    print("you got D grade")
else:
    print("you got F grade")    
"""
