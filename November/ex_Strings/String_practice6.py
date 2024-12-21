# Input = JhonDipPrta
# output = Dip
str1 = input("Enter the string :")
print("Original String is :",str1)
# get the string size
l = len(str1)
# get the middle index
mi = int(l/2)
# Get the middle index added to result
res = str1[mi-1]+ str1[mi] +str1[mi+1]
# get the last character added to result
print("New String : ", res)