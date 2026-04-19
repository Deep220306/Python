# seth methods
"""
s = {1,2,4,5,23,42,"hi"}
s.add(333)
print(s)
s.remove(1)
print(s)    
s.pop()
print(s) # the popped element is random
s.clear()
print(s) # set is empty now
"""

# set operations
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.intersection(b)) # {4, 5}
print(a.difference(b)) # {1, 2, 3}
print(a.symmetric_difference(b)) # {1, 2, 3, 6, 7, 8}

print(a|b) # union
print(a&b) # intersection
print(a-b) # difference
print(a^b) # symmetric difference
