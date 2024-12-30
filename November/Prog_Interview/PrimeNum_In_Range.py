# This is programe to print all prime number in given interval

for num in range (2,51):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)



