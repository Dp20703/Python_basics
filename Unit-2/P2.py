import array as arr 
a=arr.array("i",[1,2,3,4,5])
print(a)
a[0]=7
print(a)
a[0:2]=arr.array("i",[8,9])
print(a)