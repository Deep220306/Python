#print all even numbers from 1 to 20 
"""
l = []
for i in range(1,21):
    if i%2 == 0:
        l.append(i)
print(l)
"""
#using list comprehension
"""
l = [i for i in range(1,21) if i%2 == 0]
print(l)
"""
#using dict comprehension
"""
d = {i:i**2 for i in range(1,11)}
print(d)
"""
#using set comprehension
"""
s = {i for i in range(1,11) if i%2 == 0}
print(s)
"""
