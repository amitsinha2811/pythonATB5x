x= int(input("Enter the value of x \n"))
y = int(input("Enter the values of y \n"))

temp=x
x=y
y=temp
print("The values of x after swapping: {}".format(x))
print("The values of y after swapping: {}".format(y))