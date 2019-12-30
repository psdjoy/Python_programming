
class Car:

    wheels = 56

    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()
c1.mil = 9
Car.wheels = 90

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
