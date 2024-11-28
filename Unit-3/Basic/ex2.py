#default constructor:
class player:
    #default constructor
    def __init__(self):
        self.name  ="Darshan"
        self.age=21
        self.runs=69
    #instance method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Runs:",self.runs)
#create an istance to player class:
p1=player()
#call the method
p1.display()



#parameterized constructor:
class player2:
    #parameterized constructor
    def __init__(self,name,age,runs):
        self.name=name
        self.age=age
        self.runs=runs
    #instance method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Runs:",self.runs)
#create an istance to player2 class:
p1=player2("dp",21,55)
#call the method
p1.display()
