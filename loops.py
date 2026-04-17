#for loop
"""
a = range(1,20,1)
for i in a:
    print(i)
"""

#for loop printing 20 --> 0
"""
for i in range (20,0,-1):
    print(i)
"""

#for loop printing -15 ---> -5
"""
for i in range(-15,-4,1):
    print(i)
"""
#5 table
"""
for i in range(5,51,5):
    print(i)
"""

#user choice table
"""
num = int(input("Enter the number: "))
for i in range(num,num*11,num):
    print(i)
"""

#for loop in strings
"""
a = "Deep Pathak"
for i in range(9):
    print(i)      #prints the index of the string
"""

"""
a = "Deep Pathak"
for i in range(len(a)):
    print(a[i])      #prints the characters of the string
"""

"""
a = "Deep Pathak
for i in a:
    print(i)      #prints the characters of the string
"""

"""
for i in range (1,21):
    if i==16:
        break
    else:
        print(i)    #(Break Statement)   prints 1 to 15 and then breaks the loop when i is 16
"""

"""
for i in range (1,21):
    if i==16:
        continue
    else:        
        print(i)    #(Continue Statement)   prints 1 to 20 except 16
"""

"""
#for loop with else statement
for i in range (1,21):
    if i==16:
        print("Break is executed")
        break
    print(i)   
else:
    print("Break is not executed")
"""

"""
#questions on for loop

#1. Accept an integer and print Deep n times
n = int(input("Enter the number: "))
for i in range(n):
    print("Deep")

#2. Accept an integer and print the sum of first n natural numbers
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(i)      #prints the first n natural numbers

#3. print reverse from n to 1
n = int(input("Enter the number: "))
for i in range(n,0,-1):
    print(i)      #prints the first n natural numbers in reverse order

#4. print the table of n like 5 X 1 = 5 
n = int(input("Enter the number: "))
for i in range(1,11):   
    print(f"{n} X {i} = {n*i}")      #prints the table of n

#5. print the sum of first n numbers
n = int(input("Enter the number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i   
print(sum)      #prints the sum of first n natural numbers

#6. factorial of n
n = int(input("Enter the number: "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print(factorial)      

#7. sum on all even and odd numbers from 1 to n in a range seperately
n = int(input("Enter the number: "))
even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    if i%2==0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print(f"Sum of even numbers from 1 to {n} is: {even_sum}")
print(f"Sum of odd numbers from 1 to {n} is: {odd_sum}")


#8. check for perfect number
n = int(input("Enter the number: "))
sum = 0
for i in range(1, n):
    if n%i==0:
        sum = sum + i
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")   

#9. check for prime number
n = int(input("Enter the number: "))    
is_prime = True
for i in range(2, n):   
    if n%i==0:
        is_prime = False
        break
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

#10. reverse a string without using build in function
s = input("Enter the string: ")
reverse = ""
for i in range(len(s)-1, -1, -1):
    reverse = reverse + s[i]
print(f"Reverse of the string is: {reverse}")   

#11. palindrome string 
s = input("Enter the string: ")
reverse = ""
for i in range(len(s)-1, -1, -1):
    reverse = reverse + s[i]
if s==reverse:
    print(f"{s} is a palindrome string")
else:
    print(f"{s} is not a palindrome string")

#12. count the number of characters, numbers and special characters in a string
s = input("Enter the string: ")
char_count = 0
num_count = 0      
special_count = 0
for i in s:
    if i.isalpha():
        char_count = char_count + 1
    elif i.isdigit():
        num_count = num_count + 1
    else:
        special_count = special_count + 1   
print(f"Number of characters in the string is: {char_count}")
print(f"Number of digits in the string is: {num_count}")
print(f"Number of special characters in the string is: {special_count}")


print(dir(str)) #prints all the built in functions of string data type

"""

#while loop
"""
#1. print 1 to 10 using while loop
a = 1
while a<=10:
    print(a)
    a = a + 1

#2. seperate each digit of a number and print them on seperate lines
n = int(input("Enter the number: "))
while n>0:
    digit = n%10
    print(digit)
    n = n//10   

#3. reverse a number
n = int(input("Enter the number: "))
reverse = 0
while n>0:
    digit = n%10
    reverse = reverse*10 + digit
    n = n//10
print(f"Reverse of the number is: {reverse}")

#4. check for palindrome number
n = int(input("Enter the number: "))
reverse = 0
copy = n
while n>0:
    digit = n%10
    reverse = reverse*10 + digit
    n = n//10
if copy==reverse:
    print(f"{copy} is a palindrome number")
else:
    print(f"{copy} is not a palindrome number")
""" 

#guess the number game
"""
import random 
num = random.randint(1,10)
tries = 0
while True:
    guess = int(input("Enter your guess: "))
    tries = tries + 1
    if guess==num:
        if tries==1:
            print(f"Congratulations! You guessed the number in {tries} try.")
        else:
            print(f"Congratulations! You guessed the number in {tries} tries.")
        break
    elif guess<num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
"""