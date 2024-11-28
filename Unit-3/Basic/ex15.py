#Multiple inheritance:
#Deriving child classes from more than one parent class :

#1st base class:
class c1:
    def sum(self,a,b):
        return a+b
#2nd base class:
class c2:
    def mul(self,a,b):
        return a*b
#derived class:
class c3(c1,c2):
    def divide(self,a,b):
        return a/b

d=c3()
print(d.sum(1,3))
print(d.mul(12,3))
print(d.divide(12,3))