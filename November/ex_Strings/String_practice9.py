str1 = input("Enter the String1:")
print("Original String: ",str1)
lower =[]
upper =[]
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
str2 = ''.join(lower + upper)
print("Final String is :",str2)
