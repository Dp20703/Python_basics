#staic method:
class student:
    name="darshan"
    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b
    @staticmethod
    def info():
        return("This is a good class") 
print(student.info())