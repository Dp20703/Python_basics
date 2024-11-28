# mylist1=[10,20,30,40,50]
# mylist2=[60,70,80,90,100,90]

# if 50 in mylist1:
#     print('50 is Present')

# if 100 not in mylist1:
#     print('100 is not Present')

# #/Concatenate Lists
# print(mylist1+mylist2) 
# print(mylist1*3) 
# print(max(mylist2))
# print(mylist2.count(90))

# #  From 2 to 5
# print(mylist2[2:5]) 
# #  From 2 to 5 skip 2(second one)
# print(mylist2[2:5:2]) 

# mylist1.append(60)
# print(mylist1)

# #  Added 17 at 5th position
# mylist2.insert(5,17)
# print(mylist2)

# mylist2.pop(3)
# print(mylist2)
# mylist2.reverse()
# print(mylist2)

# mylist1.clear()
# print(mylist1)

# # x=str(3.5)
# x=int('12')
# print((type(x)))

# x=bytearray(4)
# print(x)

# thislist=['apple','banana','mango','orange']
# thislist[1]='kiwi'
# print(thislist )

# thistuple=('apple','banana','cherry')
# print(thistuple)
# print(thistuple[1])
# print(thistuple[-1])
# y=list(thistuple)
# y[-1]='kala'
# thistuple=tuple(y)
# print(thistuple)

# x=range(0,10,5)
# for n in x:
#  print(n)
#     y=range(11,20,2)
# for n in y :
#  print(n)


# thisset={'apple','banana','cherry'}
# print(thisset)
# for x in thisset:
#     print(x)
# print('banana' in thisset)
# thisset.add('orange')
# print(thisset)
# thisset.update(['orange','mango','grapes'])
# print(thisset)
# print(len(thisset))
# thisset.remove('banana')
# print(thisset)
# thisset.discard('banana')
# print(thisset)
# x=thisset.pop()
# print(x)
# print(thisset)
# thisset.clear()
# print(thisset)
# set1={'a','b','c'}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)
# print(set1)
# set1.update(set2)
# print(set1)
# del set3
# print(set3)


# thisset=set(('apple','banana','cherry'))
# print(thisset)
# set1=set([1,2,3,4,5,6,7,8,9,10])
# print(set1)
# set1.remove(5)
# set1.remove(8)
# print(set1)

# mylist=['apple','banana','cherry']
# x=frozenset(mylist)
# x[1]='mango'
# print(x)

# mydict={'ten':10,'twenty':20,'thirty':30,'fourty':40}
# print(mydict)
# print(list(mydict.keys()))
# print(list(mydict.values()))
# print(list(mydict.items()))
# mydict.update({'fifty':50})
# print(mydict)

# x=5
# print(type(x))

# a=1231
# y=100
# c=x//y
# print(c)
# a=100
# y=1
# c=x**y
# print(c)


# num=input('Enter the number ')
# name1=input('enter the name ')
# print(num)
# print(name1)
# print(type(num))
# print(type(name1))
# x,y =input('Enter the numbers:').split()
# print('First number is :',x)
# print('Second number is: ',y)
# print('Total marks are: ',int(x)+int(y))