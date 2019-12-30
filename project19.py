
def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('joy', age=28, city='dhaka', mob=2324)
