#class variable:
class player:
  #class variable:
  name="darshan"
  age=23
  #class method:
  @classmethod
  def modifty(md):
    md.name="Dp"
    md.age=22 
#create an instance to player class:
p1=player()
print("Name",p1.name)
print("age",p1.age)

#call the method:
p1.modifty()
print("Name",p1.name)
print("age",p1.age)
   
