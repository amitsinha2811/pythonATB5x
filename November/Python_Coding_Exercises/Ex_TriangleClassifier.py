side1 = float(input("Enter the length of side1 of a triangle :\n"))
side2 = float(input("Enter the length of side2 of a triangle :\n"))
side3 = float(input("Enter the length of side3 of a triangle :\n"))


if side1==side3 and side2==side3:
    print("This is a Equilateral Triangle")
elif side1==side2 and side2!=side3:
    print("This is a Isosceles Triangle ")
else:
    print("This is a Scalene Triangle")