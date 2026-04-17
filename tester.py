a = [34, 89, -43, -23, 66, -8]
largest = a[0]
second_largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
print("the largest element of the list is:", largest)
print("the second largest element of the list is:", second_largest)