num1= int(input("Enter the value of Num1: "))
num2= int(input("Enter the value of Num2 : "))
num3= int(input("Enter the value of Num3: "))

if(num1>num2) and (num1>num3):
    print(num1,"is the largest number")
elif (num2>num1) and (num2>num3):
    print(num2,"is the largest number")
else:
    print(num3, "is the largest number")