num= int(input("Enter the number to verify the armstrong number: "))

sum=0
temp  = num

while temp > 0:
    digit = temp%10
    cube = digit**3
    sum= sum + cube
    temp//=10

if sum==num:
    print("The Given number is an armstrong number")
else:
    ("The given number is not an armstrong number")