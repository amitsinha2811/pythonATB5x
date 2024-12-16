side1 = float(input("Enter the length of side1 of a triangle :\n"))
side2 = float(input("Enter the length of side2 of a triangle :\n"))
side3 = float(input("Enter the length of side3 of a triangle :\n"))

if side1>0 and side2 >0 and side3 > 0 :
    if side1 +side2 >side3 and side2 + side3 >side1 and side1 + side3 > side2:
        if side1==side3 and side2==side3:
            print("This is a Equilateral Triangle")
        elif side1==side2 and side2!=side3:
            print("This is a Isosceles Triangle ")
        else:
            print("This is a Scalene Triangle")
    else:
        print("Sum of two sides of triangle can not be greater then third side")
else:
    print(" This is not a valid lenght")