# This is programe to print all prime number in given interval
# for num in range (2,51):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print("Sum of prime num is :",sum)


def is_prime(number):
    for z in range(2,number):
        if (number%z ==0):
            return False
def add(number):
    total =0
    for z in range(2,number+1):
        if (is_prime(z)):
            total = total+z
    return total
add(number=10)




