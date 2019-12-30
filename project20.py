
a = 10
b = 3
c = 6


def something():
    a = 15
    x = globals()
    print('id(x)', id(x))
    print('x', x)
    print('id a', id(a))
    print(a)


something()
print('id(a)', id(a))
print(a)
