# Input = Muddassir ahmed
# Output = mudasir he
str = "muddassir ahmed"
print(str[0]+str[1]+str[2]+str[4]+str[5]+str[7]+str[8]+str[9]+str[11]+str[13])

print("========================================")

def print_unique_char(input_string):
    seen = set()
    for char in input_string:
        if char not in seen:
            print(char, end="")
            seen.add(char)

input_string = "muddassir ahmed"
print_unique_char(input_string)
