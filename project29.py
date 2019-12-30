class Computer:

    def __init__(self):
        self.name = "joy"
        self.age = 24

    def update(self):
        self.age = 30


c1 = Computer()
c2 = Computer()
c1.name = "hello"
c1.update()

print(c1.name, c1.age)
print(c2.name, c2.age)
