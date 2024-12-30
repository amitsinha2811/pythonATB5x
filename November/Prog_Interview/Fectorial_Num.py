# This is a program to print fectorial of a number
fectorial =1
num= int(input("Enter the value of Num here: "))
for i in range(1,num+1):
    fectorial = fectorial*i
print("The fectorial of",num,"is",fectorial)

# This a program to print fectorial of a number using recursion
def fecto(n):
    if n<=1:
        return n
    else:
        return (n)*fecto(n-1)
n= int(input("Enter the number for which you want fectorial: "))

if n<0:
    print("Please enter a valid number ")
else:
    print("The fectorial of given natural number is :",fecto(n))