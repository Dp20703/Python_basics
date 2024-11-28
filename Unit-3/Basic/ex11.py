#Teacher class:[super class/base class]
class Teacher:
    def __init__(self,schoolName):
        self.schoolName=schoolName
    def display(self):
        print("School name:", self.schoolName)
#Student class:[sub class/derived class]
class student(Teacher):
    pass #nothing to write here:
s=student("Prakash high school")
s.display()