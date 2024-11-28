class emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print("Id=",self.id)
        print("Name=",self.name)
        print("Salary=",self.salary)
class myclass:
    @staticmethod
    def mymethod(e):
        e.salary+=1000
        e.display()
        
e=emp(1001,"Raj kumar",10000.33)
myclass.mymethod(e)
