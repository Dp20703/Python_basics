# #  Import Inbuild Module
# import math
# print(math.sqrt(25))

# #Import User Define Module
# import calc
# add=calc.add(10,2)
# print(add)
# print (calc.sub(10,2))

# #Arbitrary arguments, *args
# def myfunction(*kids):
#     print("The youngest kid among the kids is:" + kids[2])

# #Keywords arguments
# myfunction("Suresh" ,"mahesh","jayesh")
# def myfunction(child3,child1,child2):
#     print("The youngest kid among the kids is:" +child2)
#     print("The youngest kid among the kids is:" +child1)
#     print("The youngest kid among the kids is:" +child3)

# myfunction(child1="Suresh" ,child3="mahesh",child2="jayesh")

# #Default parameter value
# def myfunction(country="india"):
#     print("My country name is :" +country)

# myfunction()
# myfunction("US")
# myfunction("WI")

# #Returning result from a function
# def func(a,b):
#     return a+b
# print(func(4,3)) #single value return

# def func(a,b):
#     return a*b,a/b
# print(func(3,4)) #multi-value return

# #Method
# class abc:
#     def method_abc(self):
#         print("I am the method of abc class")
# class_ref=abc()
# class_ref.method_abc()
# # abc.method_abc()

# #Function:
# def sub(a,b):
#     return(a-b)
# print(sub(10,12))
# print(sub(14,4))

# #Lambda function:
# cube=lambda x: x*x*x
# print(cube(4))

# #Filter
# list1=[1,23,34,43,5,12,24,3,43,4]
# final_list=list(filter(lambda x:x%2!=0,list1))
# print(final_list)
# # def lamb(x):
# #     return x%2!=0
# # final_list2=list(filter(lamb,list1))
# # print(final_list2)

# #map:
# list1=[1,23,34,43,5,12,24,3,43,4]
# final_list=list(map(lambda x:x*2,list1))
# print(final_list)

# #reduce:
# from functools import reduce
# li=[5,8,10,20,50,100]
# sum=reduce((lambda x,y:x+y),li)
# print(sum)
# # def lamba(x,y):
# #     return x+y
# # sum2=reduce((lamba),li)
# # print(sum2)

# #Function Decorators:
# def helllo_decorator(func):
#       def inner1():
#         print("hello ,this is before function excecution")
#         func()
#         print("This is after function execution")
#         return inner1
    
# def function_to_be_used():
#      print("This is inside the function execution")  
# function_to_be_used=helllo_decorator(function_to_be_used)

# function_to_be_used()

mylist=[1,3,45,554,4 ,9,88,434]
mylist[0]=22
# print(mylist)

mylist2=[1,2,3,4,5,6,7,8,9,10]
mylist3=[11,22,33,44,55,66,77,88]
# mylist2=mylist2+mylist3
# print(mylist2) 
#   method 1

for i in mylist3: 
    mylist2.append(i)
# print(mylist2) 
# //method 2

# list1=[1,2,3,4,5]
# list2=[11,22,33,44,55]
# for i in list1:
#     if i in list2:
#         print("overlapping")
#         break
# else:
#         print("No overlapping")
# x=2
# y=22
# list1=[1,2,3,4,5]
# list2=[11,22,33,44,55]
# for i in list1:
#     if x  in list2 :
#         print("x is  present")
#         break
# else:
#         print("x is  not present")


#cloning or slicing technique:    
# def cloning(li1):
#     # li_copy=li1[:]
#     # //Method-1

#     # li_copy=[]
#     # li_copy.extend(li1)
#     # //Method-2

#     li_copy=list(li1)
#     # //Method-3

#     return li_copy

# li1=[33,443,55,3,33]
# li2=cloning(li1)
# print("original:",li1)
# print('copy:',li2)

dict={}
dict_simple={"fruit":"mango",1:'mango2',2:'banana'}
# dic2=dict(1:"mango",2:"cherry")
# print(dic2)
# print(dict_simple[1])

# dict3=dict([1,"mango"],[2,"cherry"])
# print(dict3)
# x=dict_simple.get("fruit")
# print(x)
# dict_simple["name"]="Honda"
# print(dict_simple)

# mydict[0]="apple"
# mydict[1]="mango"
# mydict[2]=20
# print(mydict)
 
# dict_simple['fruit']="banana"
# print(dict_simple)
dict_simple2={"fruit":"mango",1:'mango2',2:'banana'}
# del dict_simple2["fruit"]
# dict_simple2.pop("fruit")
# dict_simple2.popitem()
# del dict_simple2
# dict_simple2.clear()
# print(dict_simple2) 
# dict_simple2["fruit"]="banana"
d=dict_simple2
# print(d.popitem())
# print(d.pop("fruit2",12))
# print(list(d.items())[0][0])
# print(dict_simple2)

d1={"a":10,"b":20,"c":30}
# d2={"b":200,"d":22}
d1.update([("a",20),("d",400)])
d1.update(a=1,d=22)
# d1.update(d2)
# print(d1)

def adder(*args):
   sum=0
   for n in args:
      sum=sum+n
   print("sum is :",sum)

adder(2,3,2,43)
   


def intro(**data):
    print("type of data:",type(data))
    for key,value in data.items():
     print("{} is {} ".format(key,value))

# intro(firstname="sita",lastname="sharma")

