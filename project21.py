
lst = [12, 13, 23, 54, 76, 98, 234, 1, 47, 54]


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = count(lst)

print("even: {} and odd: {}".format(even, odd))
