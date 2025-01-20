n = int(input("Enter the number for fectorial :"))
def fectorial(n):
    if n==0:
        return 1
    return n* fectorial(n-1)
print("The fectorial",n, "is ", fectorial(n))
