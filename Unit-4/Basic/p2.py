class person:
   def __init__(self):
      self.name="darshan"
      self.age=21 

   def display(self):
      print("name:",self.name)
      print("age:",self.age)

   def voting(self,age):
      try:
          if age>18:
            print("You can vote!")
          else:
            print("you can't vote")
      except:
         print("Error")
         
   
p=person()
p.display()
p.voting("djaf")