num1= int(input("Enter num1 here :"))
print("The fectors of given numbers are : ")

def Fectors(num1):
    for i in range(1,num1+1):
        if (num1%i==0):
            print(i)

print(Fectors(num1))