def search(list ,n):
   for i in range(len(list)):
        if list[i]==n:
            return True
   return False
       
list=['ramesh','suresh','Python']
n='Python'
if search(list,n):
    print("found")
else:
    print('not found')

