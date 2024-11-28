class student:
    def __init__(self,name="",age=15,marks=0):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s=student("Darshan")
s.display()
s=student("Dp",21,88)
s.display()