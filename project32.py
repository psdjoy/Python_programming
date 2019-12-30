

class Student:

    school = "Joy"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg1(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def info1():
        print("This is a student class ")


s1 = Student(20, 30, 50)
s2 = Student(30, 40, 44)

print(s1.avg1())
print(s2.avg1())
print(Student.info())
Student.info1()