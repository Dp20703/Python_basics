class duck:
    def talk(self):
        print("Quack,quack!")
class human:
    def talk(self):
        print("Good morning!")
def call_talk(obj):
    obj.talk()

x=duck()
call_talk(x)
x=human()
call_talk(x)