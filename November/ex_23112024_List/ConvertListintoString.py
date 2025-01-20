# Lst= ["A":1,"S":2,"H":3,"M":4,"I":4,"T":5]
# string= ''.join(Lst)
# print(string)

Str = "aaaabbbbbcccccddddeeeefffffggggghhhh"
sample = "abcdefgh"
count = {}.fromkeys(sample,0)

for char in Str:
    if char in count:
        count[char]+=1
print(count)
print(str(count))