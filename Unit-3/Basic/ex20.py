class Human:
    def display(self,name=None):
        if name is not None:
            print("Hello",name)
        else:
            print("Hello")
h=Human()
h.display()
h.display("dp")