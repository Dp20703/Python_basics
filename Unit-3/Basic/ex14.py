#Single inheritance:
#one parent class and one or more child classes:
class parent:
    def display(self):
        print("parent class")

class boy(parent):
    def display(self):
        super().display()
        print("boy class")
class girl(parent):
    def display(self):
        print("girl class")
b=boy()
b.display()
g=girl()
g.display()