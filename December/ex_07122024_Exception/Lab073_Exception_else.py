print("========Star of the Program=============")
try:
    a= int(input("Enter the Num1: "))
    b= int(input("Enter the num2: "))
    c=a/b
except ValueError as d:
    print(d)
except ZeroDivisionError as d:
    print(d)
else:
    print("Output is", c)
finally:
    ("This code will be always executed")
print("========End of the Program=============")