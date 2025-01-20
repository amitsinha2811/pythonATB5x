def is_prime(number):
    for z in range(2,number):
        if (number%z ==0):
            return False
    return True
def add(number):
    total =0
    for z in range(2,number+1):
        if (is_prime(z)):
            total = total+z
    return total
print(add(number=10))