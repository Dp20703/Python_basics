#Program for class variable:
class sample:
    var =10 # class variable
    #class method
    @classmethod
    def modify(cls):
        cls.var+=1
s1=sample()
s2=sample()
print("X in s1 ",s1.var)
print("X in s2 ",s2.var)

#modify x in s1....
s1.modify()
print("X in s1 ",s1.var)
print("X in s2 ",s2.var)

#Program for instance variable:
class sample:
    def __init__(self):
        self.x=20 #instance variable
    #instance method
    def modify(self):
        self.x+=1
s1=sample()
s2=sample()
print("X in s1 ",s1.x)
print("X in s2 ",s2.x)

#modify x in s1....
s1.modify()
print("X in s1 ",s1.x)
print("X in s2 ",s2.x)