# a= "how modi is changing the india's economy"
# vowels = "aeiou"
#
# count = {}.fromkeys(vowels,0)
#
# for char in a:
#     if char in count:
#         count[char]+=1
# print(count)
# print("=============================================")
# def common_letters():
#     str1 = input("Enter first string here :")
#     str2 = input("Enter second string here :")
#     s1=set(str1)
#     s2= set(str2)
#     lst=s1 & s2
#     print("common letters in both strings are", lst)
#
# common_letters()
#
# print("===============================================")

a= "how modi is changing the india's economy"
letter = "abcdefghijklmnopqrstuvwxyz"

count = {}.fromkeys(letter,0)

for char in a:
    if char in count:
        count[char]+=1
print(count)
