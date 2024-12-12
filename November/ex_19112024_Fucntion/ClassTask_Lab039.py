# Write a program to print sum of three num from user input
# if user does not enter take default input as 100,200,300
a = int(input("Enter the value of a: \n"))
b = int(input("Enter the value of b: \n"))
c = int(input("Enter the value of c: \n"))

def sum_of_three_num(a=100,b=200,c=300):
    return a+b+c
result= sum_of_three_num(a, b,c)
print(result)
result = sum_of_three_num()
print(result)
