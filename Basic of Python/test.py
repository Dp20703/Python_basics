# import sys
# print ('number of arguments ',len(sys.argv),'Arguments')
# print ('list of arguments ',str(sys.argv))

import os
os.system('cls')
# x=int(input('Enter the first number'))
# y=int(input('Enter the second number'))
# if x>y:
#     print('X is max')
# elif(y>x):
#     print('Y is max')
# else:
#     print('Both are equal')

# x=1
# sum=0
# while(x!=6):
#     y=int(input('Enter the number: '))
#     sum=sum+y
#     x=x+1
#     print(x)
    # print('Sum is :',sum)

# print('Sum is : ',sum)

# for i in range(1,11):
#     print(i)

# x=int(input('Enter the number you want to multiple:'))
# for i in range(1,11):
#     print(x,'*',i,"=",x*i)

# for i in range(11,0,-1):
#     print(i)

# obj=['red','big','tasty']
# fruits=['apple','banana','cherry']

# for x in obj:
#     for y in fruits:
#         print( x ,y)

# fruits=['apple','banana','cherry']
# for x in fruits:
#     print(x)
#     if x=='banana':
#         continue
#     else:
#         print('else block')
#     print('break is over')
   
# print('Loop is over')

# fruits=['apple','banana','cherry']
# for x in fruits:
#     if x=='banana':
#         continue
#     print(x)
# for x in [0,2,4]:
#     pass

# x ='hello'
# assert x=='goodbye'

# def myfun():
#     return 3+3
# print(myfun())

def max(x,y):
    if x>y:
        return x
    else :
        return y
a=int(input('Enter the first number: '))
b=int(input('Enter the Second number: '))
c=max(a,b)
print("Max is: ",c)