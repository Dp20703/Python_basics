# number=int(input("Enter the number:"))
def plus_one(number):
    def add_One(number):
        return number+3
    result=add_One(number)
    return result
print(plus_one(3))