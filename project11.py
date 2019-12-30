import array as arr

vals = arr.array('i', [1, 2, 3, 4, 5, 6])

newArray = arr.array(vals.typecode, (pow(a, 3) for a in vals))
for e in newArray:
    print(e)
