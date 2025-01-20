def string(data):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in data if not char.isalpha() or char in  vowels])
    return result
print(string(data= "Python and data science"))