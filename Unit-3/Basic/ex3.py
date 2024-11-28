#parameterized constructor:
class player2:
    #parameterized constructor
    def __init__(self,name,age,runs):
        self.name=name  #instance variable
        self.age=age    #instance variable
        self.runs=runs  #instance variable
    #instance method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Runs:",self.runs)
#create an istance to player2 class:
p1=player2("Dp",21,55)
p2=player2("kp",20,25)
#call the method
p1.display()
#call the method
p2.display()