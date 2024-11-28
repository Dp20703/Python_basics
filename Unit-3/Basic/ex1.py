class player:
    def __init__(self):
        self.name="Sachin"
        self.age=25
        self.runs=79
#instance method:
    def display(self): 
     print("Name:",self.name)
     print("Age:",self.age)
     print("Runs:",self.runs)

#create an instance to player class:
p1=player()
#calll the method:
p1.display()
