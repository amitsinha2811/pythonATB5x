# Str = "Donald Trump become the 47th President of USA"
# vowels = "aeiouAEIOU"
# count=0
# for char in Str:
#     if char in vowels:
#         count = count + 1
# print(count)
Str = "Donald Trump become the 47th President of USA"
vowels = "aeiouAEIOU"
count = {}.fromkeys(vowels,0)

for char in Str:
    if char in count:
        count[char]+=1
print(count)
# This is program to count the number of consonants in string
# Str = "Donald Trump become the 47th President of USA"
# consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# count=0
# for char in Str:
#     if char in consonants:
#         count = count + 1
# print(count)