num1= int(input("Enter num1 here :"))
num2= int(input("Enter num2 here :"))

def CalcHCF(num1,num2):
    if num1>num2:
        least= num2
    else:
        least= num2
    for i in range(1,least+1):
        if (num1%i==0) and (num2%i==0):
            hcf=i
    return hcf
print(CalcHCF(num1,num2))
