
def update(x):
    x[1] = 25
    print(id(x))
    print('x ', x)


a = [10, 20, 30]
print(id(a))
update(a)
print('a', a)
