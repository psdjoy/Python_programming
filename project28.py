class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configure is", self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('Rezen', 64)

com1.config()
com2.config()
