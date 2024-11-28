minimum=int(input("Enter the minimum number: "))
maximum=int(input("Enter the maximum number: "))

even_total=0
odd_total=0

for num in range(minimum,maximum+1):
    if num%2==0:
        even_total=even_total+num
    else:
        odd_total=odd_total+num

print("The Sum of Even numbers from 1 to {0}={1}".format(num,even_total))
print("The Sum of Odd numbers from 1 to {0}={1}".format(num,odd_total))
