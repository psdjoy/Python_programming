from numpy import *

arr1 = array([1, 2, 3, 4])

k = len(arr1)
laa = arr1[k-1]
for i in range(k):
    if laa > arr1[i]:
        laa = arr1[i]


print(laa)
