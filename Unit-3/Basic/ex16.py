#Method resolution order (MRO):
class a(object):
    def method(self):
        print("A Class method")
        # super().method()
class b(object):
    def method(self):
        print("B Class method")
        # super().method()
class c(object):
    def method(self):
        print("C Class method")
        # super().method()
class x(a,b):
    def method(self):
        print("X Class method")
        super().method()
class y(b,c):
    def method(self):
        print("Y Class method")
        super().method()
class p(x,y,c):
    def method(self):
        print("P Class method")
        super().method()
newP=p()
print(p.mro())
newP.method()