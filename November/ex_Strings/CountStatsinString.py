import re


str1 = "python is Number 1"

digitCount = re.sub("[^0-9]", "",  str1)
letterCount = re.sub("[^a-zA-z]","", str1)
spaceCount = re.findall("[ \n]", str1)

print("Total number of digit is :", len(digitCount))
print("Total no of letters are :", len(letterCount))
print("Total Number of white space are:  ", len(spaceCount))