num1= int(input("Enter num1 here :"))
num2= int(input("Enter num2 here :"))
print("Press 1 for addition :")
print("Press 2 for Substarction :")
print("Press 3 for Multiplication :")
print("Press 4 for Division :")
choice = int(input("Enter your choice from 1-4:"))
if choice==1:
    print("Sum of two number is:",num1+num2)
elif choice==2:
    print("Differenec of two number is: ", num1-num2)
elif choice==3:
    print("Multiplication of two number is:",num1*num2)
elif choice==4:
    print("Division of two number is:",num1/num2)
else:
    print("Please choose correct option")


