class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summer(self):
        return self.a + self.b


x = int(input("Enter number 1 "))
y = int(input("Enter number 1 "))

ac = Sum(x, y)
print(ac.summer())
