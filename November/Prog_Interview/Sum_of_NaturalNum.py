# This a program to print sum of natural numbers
sum=0
for i in range(1,100):
    sum=sum+i
print("Sum of Natural number are ",sum)

# This is program to print sum of natural numbers using recursion
def sum(n):
    if n<=1:
        return n
    else:
        return (n)+sum(n-1)
n= int(input("Enter the number for which you want sum: "))

if n<0:
    print("Please enter a valid number ")
else:
    print("The sum of given natural number is :",sum(n))