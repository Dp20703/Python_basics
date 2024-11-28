class father:
    def height(self):
        print("Height is 6.0 foot")
class mother:
    def complexion(self):
        print("Complexion is fair")

class child(father,mother):
    pass
c=child()
c.height()
c.complexion()
        