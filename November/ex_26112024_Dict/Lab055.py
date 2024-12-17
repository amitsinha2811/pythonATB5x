import json

from November.ex_23112024_Lambda.Lab048 import result

string = "automation"
char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
print("=======================================")
result = json.dumps(string)
print("strings1", result)

