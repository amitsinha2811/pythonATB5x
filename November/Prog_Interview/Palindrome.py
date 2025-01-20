a= input("Enter a string here :")
rev = a[::-1]
if a==rev:
    print(a,"is a palindrome sequence")
else:
    print(a,"is not a palindrome sequence")

#  This is a program to write to check any number is palindrom or not

def Is_palindrome(num):
    temp = num
    rev = 0
    while (temp>0):
        digit = temp%10
        rev = rev*10+digit
        temp = temp//10
    if num ==rev:
        return True
    else:
        return False

print(Is_palindrome(123321))