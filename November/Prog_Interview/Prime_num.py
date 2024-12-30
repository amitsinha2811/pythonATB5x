num=int(input("Enter the value of num: "))
if num>=2:
    for i in range(2, num):
        if (num%i)==0:
            print(num, "is a not prime number")
            break
    else:
        print(num, "is a prime number")

