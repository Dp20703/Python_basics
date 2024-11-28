#parent class:
class parent:
    #constructor:
    def __init__(self,name) :
        self.name=name
    #instance method to get name:
    def getName(self):
        return self.name
    #To check if this person is a child or not:
    def isChild(self):
        return False

#child class or subclass:
class child(parent):
    #here we return true:
    def isChild(self):
        return True

p=parent("Mr.Darshan") #an object of parent class
print("Is",p.getName(),"a child ?",p.isChild())
p=child("Mr.dp") #an object of child class
print("Is",p.getName(),"a child ?",p.isChild())