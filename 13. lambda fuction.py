#normal code
def add(x,y):
    return x+y
print(add(2,3))

#lambda function
add=lambda x,y:x+y
print(add(2,3))

#lamda function with if else
check_even=lambda x: "Even" if x%2==0 else "Odd"
print(check_even(4))
print(check_even(5))

