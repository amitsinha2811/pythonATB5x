year= int(input("Enter the year in YYYY format : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is a leap year")
else:
    print(year, "is not a leap year")