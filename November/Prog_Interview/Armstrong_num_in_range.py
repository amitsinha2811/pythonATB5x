# This is the programe to print armstrong number in renge

for num in range(0,100000):
    order = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp%10
        sum += digit ** order
        temp //= 10
    if num==sum:
        print(num)