Year = int(input("Enter the year in YYYY format :"))
if ( Year%4==0 and Year % 100!=0) or (Year % 400 ==0):
    print("This is a Leap  year.", Year)
else:
    print("This is not a Leap Year", Year)