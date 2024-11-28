class players:
   #mutator method:
   def setName(self,name):
      self.name=name
   #accessor method:
   def getName(self):
      return self.name
   #mutator method:
   def setRuns(self,runs):
      self.runs=runs
   #accessor method:
   def getRuns(self):
      return self.runs
n=int(input("How many players?"))
i=0
while(i<n):
   p=players()
   name=input("Enter Name:")
   p.setName(name)
   runs=input("Enter Runs:")
   p.setRuns(runs)
   print("Hi",p.getName())
   print("You Scored:",p.getRuns(),"runs")
   i+=1
   print("---------------------")