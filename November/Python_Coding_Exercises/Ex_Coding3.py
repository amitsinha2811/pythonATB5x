# This Programme is based on fizzbuzz on python
num = int(input("Please Enter the number :\n"))
if num%3==0 and num%5!=0:
    print("Fizz")
elif num%5==0 and num%3!=0:
    print("Buzz")
elif num%3==0 and num%5==0:
    print("FizzBuzz")
else:
    print("Try Again")

