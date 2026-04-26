d = {1: "one", 2: "two", 3: "three"}
print(d[1]) # one

#crud operations
"""
d[4] = "four" # create
print(d) 
d[2] = "TWO" # update
print(d) 
del d[3] # delete
print(d) 
"""

#traversal
"""
for i in d:
    print(i) #gives keys

for i in d:
    print(d[i]) #gives values

for i in d.values():
    print(i) #gives values

for i in d.items():
    print(i) #gives key value pairs as tuples

for key, value in d.items():
    print(key, value) #gives key and value separately
"""

#dictionary methods
"""
# deep copy and shallow copy
d1 = d.copy() # shallow copy
d2 = d # deep copy

#get method
d0 = d.get(1) 
print(d0) # one
d9 = d.get(9)
print(d9) # None

""" 

#merge 2 dictionaries
"""
d1 = { 1: 10, 2: 20 }
d2 = { 3: 30, 4: 40 }
for i in d1:
    d1[i] = d2[i]
print(d1) 
"""

#sum of all values in a dictionary
"""
d = { 1: 10, 2: 20, 3: 30 }
total = 0
for i in d:
    total += d[i]
print(total) 
"""

#counting frequency of elements in a list using dictionary
"""
a = [1, 2, 2, 3, 3, 3]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1    
print(d)
"""

#combine 2 dictionaries by adding values of common keys
"""
d1 = { 1: 10, 2: 20, 3: 30 }
d2 = { 2: 200, 3: 300, 4: 400 }
d3 = {}
for i in d2:
    if i in d1:
        d3[i] = d1[i] + d2[i]
    else:
        d3[i] = d2[i]   
print(d3)
"""

