#class method:
class student:
    name="darshan"
    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b
    @classmethod
    def info(cls):
        return cls.name    
print(student.info())