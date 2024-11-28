import P13
print("SALARY PROGRAM")
name=str(input("Enter name of the employee:"))
basic=int(input("Enter Basic Salary:"))
netpay=P13.net_Salary
print(f'Net Salary: {netpay}')
grosspay=P13.gross_Salary
print(f'Gross salary:{grosspay}')