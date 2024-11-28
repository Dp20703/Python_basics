import os

def findfiles(filename,searchpath):
    result=[]
#walking topdown from root:
    for root,dir,files in os.walk(searchpath):
        if filename in files:
            result.append(os.path.join(root,filename))
    if result==[]:
        return("No such file found")
    else:
        return result
    
#creating file:
file=input("Enter the name of file with extension for file creation:")
f=open(file,'w')
f.close()

#find the file:
file=input("Enter the name of file with extension for searching:")
print(findfiles(file,os.getcwd()))
