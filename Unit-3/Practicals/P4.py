class student:
    #mutator method:
    def setname(self,name):
        self.name=name
    #acessor method:
    def getname(self):
        return self.name
    #mutator method:
    def setmarks(self,marks):
        self.marks=marks
    #acessor method:
    def getmarks(self):
        return self.marks
    
n=int(input("How many students?"))
i=0 
while(i<n):
    s=student()
    name=input("Enter name:")
    s.setname(name)
    marks=input("Enter your marks:")
    s.setmarks(marks)
    print("hiii ",s.getname())
    print("Your marks :",s.getmarks())
    i+=1
    print('------------------------------')