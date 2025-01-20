def first_non_repeating_char(str):
    for i in str:
        if str.count(i)==1:
            return i
    return None

str = input("Enter your string here :")
print("first non repeating char is:",first_non_repeating_char(str))