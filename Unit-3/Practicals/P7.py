import sys
class bank(object):
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
            if self.balance<amount:
              print("Low balance,Cannot withdraw")
            else:
                 self.balance-=amount
                 return self.balance
#crate an account with given name and balance 0.0:
name=input("Enter bank name:")
b=bank(name)
while(True):
    print("d/d -Deposit,w/w -withdrawal,e/E -exit:")
    choice=input("Enter your choice:")
    if choice=="e" or choice=="E":
        sys.exit()
    amount=float(input("Enter amount:"))
    if choice=='d' or choice=="D":
        print("Balance after deposit:",b.deposit(amount))
    elif choice=='w' or choice=="W":
        print("Balance after withdrawals:",b.withdraw(amount))


