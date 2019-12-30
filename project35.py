class A:

    def __init__(self):
        print("A init")

    def feture1(self):
        print("feature 1 working")

    def feture2(self):
        print("feature 2 working")


class B:

    def __init__(self):
        print("B Init")

    def feture1(self):
        print("feature 3 working")

    def feture4(self):
        print("feature 4 working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

    def feat(self):
        super().feture4()


a1 = C()
a1.feat()
