str="This is a game"
def reverse_string(str):
    result = ""
    for char in str:
        result = char + result
    return result

print(reverse_string(str))