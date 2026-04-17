#list
"""
a = [1,2,3,4,5]
print(a)
print(a[0])
print(a[1]) 
"""
#traverse the list
"""
for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])
"""
#list slicing
"""
print(a[0:3]) #prints 0,1,2
print(a[2:]) #prints 2,3,4
print(a[:3]) #prints 0,1,2
print(a[:]) #prints all elements
"""

#methods of list
"""
print(dir(list))
"""

#list is mutable
"""
a = [1,2,3,4,5]
a[0] = 10
print(a)
"""

#print posuitive and negative of the list 
"""
a = [34, 89, -43, -23, 66, -8]
print("these are the positive elements of the list:")
for i in a:
    if i > 0:
        print(i)
print("these are the negative elements of the list:")
for i in a:
    if i < 0:
        print(i)
"""

# mean of the list
"""
a = [34, 89, -43, -23, 66, -8]
sum = 0
for i in a:
    sum += i    
mean = sum / len(a)
print("the mean of the list is:", mean)
"""

#largest and smallest element of the list
"""
a = [34, 89, -43, -23, 66, -8]
largest = a[0]
largest_index = 0
smallest = a[0]
smallest_index = 0
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        largest_index = i
    if a[i] < smallest:
        smallest = a[i]
        smallest_index = i
print("the largest element of the list is:", largest)
print("the index of the largest element is:", largest_index)
print("the smallest element of the list is:", smallest)
print("the index of the smallest element is:", smallest_index)
"""
#largest and 2nd largest element of the list
"""
a = [34, 89, -43, -23, 66, -8]
largest = a[0]
second_largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
    elif a[i] > second_largest:
        second_largest = a[i]
print("the largest element of the list is:", largest)
print("the second largest element of the list is:", second_largest)
"""

#list sorted in ascending order or not
"""
a = [34, 89, -43, -23, 66, -8]
fir i in range(len(a)-1):
    if a[i] > a[i+1]:
        print("the list is not sorted in ascending order")
        break
else:
    print("the list is sorted in ascending order")
"""

