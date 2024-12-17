import math

result1 = lambda a,b : a+b
print(result1(10,5))
result2 = lambda a,b : a-b
print(result2(10,5))
result3 = lambda a,b : a*b
print(result3(10,5))
result4 = lambda a,b : a/b
print(result4(10,5))

op2 = lambda : math.pow(int(input("Enter the num \n")),2)
print(op2())