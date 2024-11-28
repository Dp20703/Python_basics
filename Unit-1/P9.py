choice=0
while(choice!=5):
    print('1.Find area of circle')
    print('2.Find area of triangle')
    print('3.Find area of square and rectangle')
    print('4.Find Simple Interest')
    print('5. Exit')
    choice=int(input("Enter your choice: "))
    if choice==1:
      PI=3.14
      radius=float(input("Please Enter the radius of a circle: "))
      area=PI*radius*radius
      circumference=2*PI*radius
      print('Area of a circle =',area)
      print('Circumference of circle =',circumference)

    elif choice==2:
       a=float(input("Enter the First side: "))
       b=float(input("Enter the Second side: "))
       c=float(input("Enter the Third side: "))
       s=(a+b+c)/2
       area=(s*(s-a)*(s-b)*(s-c)**0.5)
       print('Area of the triangle =',area)

    elif choice==3:
       side=int(input("Enter the side length of Square: "))
       area_square=side*side
       print("The Area of Square= ",area_square)
       width=float(input("Please Enter the width of a Rectangle: "))
       height=float(input("Please Enter the height of a Rectangle: "))
       Area=width*height
       perimeter=2*(width*height)
       print('Area of a Rectangle is:  ',Area)
       print('Perimeter is: ',perimeter)
    elif choice==4:
       p=int(input("Enter p: "))
       r=int(input("Enter r: "))
       n=int(input("Enter n: "))
       i=(p*r*n)/100
       print(i)
    elif choice==5:
       exit()
    else:
       print('Bye Bye \n')
       
       


