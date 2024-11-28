class student:
    def __init__(self,id,name,marks) :
        self.id=id
        self.name=name
        self.marks=marks
    def display(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Marks:",self.marks)

class user:
    @staticmethod
    def show(s):
        s.marks+=10 #increment marks by 10
        s.display()

s=student(1,"Darshan",55)
user.show(s)