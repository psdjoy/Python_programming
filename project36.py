

class Pycharm:

    def execute(self):
        print("Running")


class Myeditor:
    def execute(self):
        print("another")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = Myeditor()
lap1 = Laptop()
lap1.code(ide)
