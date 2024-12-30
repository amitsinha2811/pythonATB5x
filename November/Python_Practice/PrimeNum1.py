'''def is_prime(num):
    if num <2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
            return False
    return True

num = int(input("Enter a number:"))

if is_prime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")'''

num = int(input("Enter the number :"))
if num==1 or num==2:
    print(num, "is not a prime number")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
else:
    print(num,"is not a prime number")
