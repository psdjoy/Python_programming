

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "Hp"
            self.ram = 8

        def show(self):
            print(self.brand, self.ram)


s1 = Student("Joy", 2)
s2 = Student("Paro", 3)

s1.show()
s2.show()

lap1 = Student.Laptop()
lap1.show()
