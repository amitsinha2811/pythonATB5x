def reverse_string(data):
    result = ""
    for char in data:
        result = char + result
    return result


print(reverse_string(data = "python"))