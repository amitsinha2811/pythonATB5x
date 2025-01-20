str = input("Enter your string here: ")
try:
    num = int(input("Enter your num here:"))
    print(str + num)
except(ValueError,TypeError) as a:
    print(a)