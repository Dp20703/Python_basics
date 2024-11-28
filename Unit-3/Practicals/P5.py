class student:
    marks=10
    @classmethod
    def modify(marks,name):
        print("{} scored {} marks.".format(name,marks.marks))
s=student()
s.modify("darshan")
s.modify("karan")