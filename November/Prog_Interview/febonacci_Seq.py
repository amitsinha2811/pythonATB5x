'''a=0
b=1
num=int(input("Enter a number to obatain the febonacci sequence: "))
if num==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)'''
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter the number for which you want fibonacci Sequence :"))
if n<=0:
    print("enter a positive number")
else:
    print("Febonacci Sequence")
    for i in range(0,n):
        print(fibo(i))
