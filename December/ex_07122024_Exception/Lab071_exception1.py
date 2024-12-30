# x=10/0 => ZeroDivisionError
#   x=5337 => Indentation Error
# print(1+"A") => Type error unsupported error
# print(int("a")) Value Error
# my_list = [1,2,3,3]
# print(my_list[5]) => Index error : List index out of range
# while True print("Hello world") => Syntax Error

print("========Star of the Program=============")
try:
    a= int(input("Enter the Num1: "))
    b= int(input("Enter the num2: "))
    c=a/b
    print("Result of Division is",c)
except Exception as d:
    print(d)
print("========Star of the Program=============")

