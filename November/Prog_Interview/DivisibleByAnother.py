# 1st way  to print divisible number by another num
'''num1= int(input("Enter num1 here :"))
num2= int(input("Enter num2 here :"))

if num1%num2==0:
    print(num1,"is divisible by",num2)
else:
    print(num1, "is not divisible by", num2)'''
# 2nd Way to print divisible number by another num
'''print("The numbers divisible by 13 are :")
for i in range(1,100):
    if i%13==0:
        print(i)'''
# 3rd way  to print divisible number by another num

l= [24,26,35,39,45,65,78,87,94]

result = list(filter(lambda x: x%13==0, l))
print("The numbers divisible by 13 are :",result)