str1 = input("Enter the string1 :")
str2 = input("Enter the string2 :")
print("Original String1 is :",str1)
print("Original String2 is :",str2)
# get the string size
l = len(str1)
# get the middle index
mi = int(l/2)
x = str1[:mi:]

x = x + str2

x= x + str1[mi:]

print("After appending the string in middle :", x)