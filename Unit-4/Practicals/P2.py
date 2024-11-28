a=eval(input('Enter a division:'))
b=eval(input('Enter a divisior:'))

try:
    ans=a/b
except (SystemError,TypeError):
    print("error")
else:
    print("Answer: ",ans)