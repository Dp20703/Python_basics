class parent:
    def __init__(self,txt):
        self.msg=txt
    def printMsg(self):
        print(self.msg)
        print("From parent class")

class child(parent):
    def __init__(self,txt):
        super().__init__(txt)
    def printMsg(self):
        super().printMsg()
        print("From child class")
x=child("Hello kem chho?")
x.printMsg()