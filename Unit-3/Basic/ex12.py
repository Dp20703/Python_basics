class teacher:
    def __init__(self,schoolname):
        self.schoolname=schoolname
    def display(self):
        print("School name is ",self.schoolname)

class student(teacher):
    def __init__(self, name,std,schoolname):
        self.name=name
        self.std=std
        self.schoolname=schoolname

    def display(self):
        print("Name is ",self.name)
        print("std is ",self.std)
        print("school name is ",self.schoolname)

s=teacher("prakash high school")
s.display()
s=student("dp",12,"Mp pandya")
s.display()
