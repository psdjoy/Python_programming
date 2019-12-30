
def greet():
    print('good morning')


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


greet()
r1, r2 = add_sub(4, 6)

print(r2)
