import math
a = int(input("Enter the length of side1 :"))
b = int(input("Enter the length of side2 :"))
c = int(input("Enter the length of side3 :"))
if a+b>c and b+c>a and a+c>b:
    s= (a+b+c)/2
    Ar =math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The are of the Triangle is :",Ar)
else:
    print("Please enter valid side of triangle")

