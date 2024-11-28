class myclass:
    n=0
    def __init__(self):
        myclass.n+=1

    @staticmethod
    def noOfInstance():
        print("Number of instances created are :",myclass.n)
obj1=myclass()
obj2=myclass()
obj3=myclass()
obj4=myclass()
myclass.noOfInstance()
