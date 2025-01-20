# Str = "Donald Trump become the 47th President of USA"
# vowels = "Dd"
# count=0
# for char in Str:
#     if char in vowels:
#         count = count + 1
# print(count)

def compress(s):
    n = len(s)
    new_s = ''
    count = 1
    for i in range(n-1):
        if s[i]==s[i+1]:
            count +=1
        else:
            new_s = new_s + s[i] + str(count)
            count = 1
    new_s = new_s +s[n-1] + str(count)
    return new_s

s = "aaabbbbcccccdddddeeeeeffffggggghhhh"
print(compress(s))