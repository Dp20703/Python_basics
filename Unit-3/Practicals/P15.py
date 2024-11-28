class dog:
    def bark(self):
        print("Bow Wow")
class duck:
    def talk(self):
        print("Quack quack")
class human:
    def talk(self):
        print("hii good morning")
#check the obj and calls talk() method:
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
    else:
        print("wrong object passed")
x=duck()
call_talk(x)
x=human()
call_talk(x)
x=dog()
call_talk(x)