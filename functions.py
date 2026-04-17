# different types of arguments
"""
#position arguments
def add(a, b):
    return a + b
print(add(2, 3))  

#keyword arguments
def greet(name, message):
    return f"{message}, {name}!"
print(greet(message="Hello", name="Alice"))

#default arguments
def power(base, exponent=2):
    return base ** exponent
print(power(3))
print(power(3, 3))
"""
#palindrome check
"""
def is_palindrome(s):
    rev=""
    for i in range (len(s)-1, -1, -1):
        rev = rev + s[i]

    if rev == s:
        print("Palindrome")
    else:
        print("Not a palindrome")
is_palindrome("madam")
is_palindrome("arya")
"""