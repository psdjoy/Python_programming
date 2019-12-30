

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        print(self.m1, self.m2)

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


a = Student(56, 78)
print(a.sum(7, 8, 78))
