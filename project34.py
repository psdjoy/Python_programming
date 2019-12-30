

class A:
    def feture():
        print("feature 1 working")

    def feture2(self):
        print("feature 2 working")


class B:

    def feture3(self):
        print("feature 3 working")

    def feture4(self):
        print("feature 4 working")


class C(A, B):

    def feture5(self):
        print("feature 5 working")


a1 = A()
b1 = B()
c1 = C()

a1.feture1()
a1.feture2()
b1.feture3()
b1.feture4()
c1.feture1()