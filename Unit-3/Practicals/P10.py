class square:
    def __init__(self,x):
        self.x=x
    def area(self):
        print("Area of square is ", self.x*self.x)

class rectangle(square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        super().area()
        print("Area of rectangle is ",self.x*self.y)
a,b=[float(x) for x in input("Enter length and breadth:").split()]
r=rectangle(a,b)
r.area()