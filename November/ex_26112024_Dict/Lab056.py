# Write a function that returns the maximum values of a dictionary
# {"a":10, "b":20, "c":30}

def max_value_dict(dictionary):
    return max(dictionary.values())
def min_value_dict(dictionary):
    return min(dictionary.values())

print(max_value_dict({"a":10, "b":20, "c":30}))
print(min_value_dict({"a":10, "b":20, "c":30}))