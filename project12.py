from array import *
arr = array('i', [])
length = int(input('Enter the length '))

for i in range(length):
    x = int(input('Enter the value '))
    arr.append(x)

print(arr)

k = int(input("Enter the required value "))
r = 0
for e in arr:
    if e == k:
        print(r)
        break
    r += 1

print(arr.index(k))

