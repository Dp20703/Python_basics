a=int(input('Enter a division:'))
b=int(input('Enter a divisior:'))

try:
    ans=a/b
except ZeroDivisionError:
    print("zero divison error")
else:
    print("Answer: ",ans)