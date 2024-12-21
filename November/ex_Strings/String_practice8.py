str1 = input("Enter the string1 :")
str2 = input("Enter the string2 :")
print("Original String1 is :",str1)
print("Original String2 is :",str2)
# get the string size of str1
l = len(str1)
# get the middle index of str1
mi1 = int(l/2)
# get the string size of str2
l = len(str2)
# get the middle index of str2
mi2 = int(l/2)
x=str1[0]+str2[0]+str1[mi1]+str2[mi2]+str1[-1]+str2[-1]
print("New String after combining two string is : ",x)
