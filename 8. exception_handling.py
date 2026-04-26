#exception handling

#try
"""
a = int(input("Enter a number: "))
try:
    print(10/a)
except ZeroDivisionError:
    print("Cannot divide by zero")
print("Division done")
"""

# exception as err
"""
a = int(input("Enter a number: "))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an error as {err}")
print("Division done")
"""

#NameError
"""
a =(input("Enter a number: "))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an error as {err}")
print("Division done")
"""

#else
"""
a = int(input("Enter a number: "))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an error as {err}")
else:
    print("no exception occurred")
print("Division done")
"""

#raise
"""
a = int(input("Enter age: "))
if a<10 or a>18:
    raise Exception("Age must be between 10 and 18")
else:
    print("Age is valid")
"""
