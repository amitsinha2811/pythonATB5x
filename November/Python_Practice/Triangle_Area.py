# Take user input for sides of triangle
s1 = float(input("Enter the value for side1 \n"))
s2 = float(input("Enter the value for side2\n"))
s3 = float(input("Enter the value of side3\n"))
#Triangle Criteria1
if s1>0 and s2>0 and s3>0:
    #Triangle Criteria2
    if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:

    # Calculate the semi perimetre of triangle
        s = (s1+s2+s3)/2
        print(s)

        Triangle_area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
        print("Area of Triangle is %0.2f :"  %Triangle_area)
    else:
        print("The sum of two side of triangle can not exceeds the third side, Please input the valid length")
else:
    print("The side of triangle can not be -ve")


