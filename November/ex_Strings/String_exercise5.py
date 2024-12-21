str1 = 'James'
print("Original String is :",str1)

# Get the first character
res = str1[0]

# get the string size
l = len(str1)
# get the middle index
mi = int(l/2)
# Get the middle index added to result
res = res + str1[mi]
# get the last character added to result

res = res + str1[l-1]
print("New String : ", res)

