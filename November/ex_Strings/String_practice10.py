str1 = input("Enter the String1:")
print("Original String: ",str1)
def count_char_digit_symbols(str1):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in str1:
        if char.isalpha():
            char_count=char_count +1
        elif char.isdigit():
            digit_count = digit_count +1
        else:
            symbol_count = symbol_count +1
    print("Char = ",char_count)
    print("Digit = ",digit_count)
    print("Symbols = ",symbol_count)

print(("Total count of Char, Digit and Symbols \n"))
count_char_digit_symbols(str1)
