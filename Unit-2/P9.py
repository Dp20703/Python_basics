#Positonal argument
def positional(ram ,shyam ,harish):
    print(ram,shyam,harish)
a='ram'
b='shyam'
c='harish'
positional(a,b,c)

#keyword Arguement:
def keyword(ram,shyam,harish):
    print(ram,shyam,harish)
a='ram'
b='shyam'
c='harish'
keyword(ram=a,shyam=b,harish=c)

#Default Arguement:
def keyword(ram,shyam,harish='harish'):
    print(ram,shyam,harish)
a='ram'
b='shyam'
keyword(ram=a,shyam=b)
