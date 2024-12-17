# Input = muddasir ahmed
# Output = mudasir he
import json
import pprint

string = "muddasirahmed"
char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
print("=======================================")
char_count["m"]=1
char_count["d"] =1
char_count["a"] =1
print(char_count)
print("==========================================")
result = pprint.pformat(char_count)
print("String1",result)
