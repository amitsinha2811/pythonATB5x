def is_leap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))

for i in range(1, n+1):
    print(i, end=" ")