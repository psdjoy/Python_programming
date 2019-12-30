class Computer:

    def __init__(self):
        self.name = "joy"
        self.age = 24

    def compare(self, other):

        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c1.age = 24

if c1.compare(c2):
    print("they are same")
