#'''punc='''!()-[]{};:"<>./?@#$%^&*_~'''
'''a= input("Enter a string here :")

empty_str=""

for i in a:
    if i not in punc:
        empty_str=empty_str+i
print(empty_str)'''

str = "Apple are green and Sweet"
a= "Apple"
if a in str:
    print("Apple are sweet and green")
else:
    pass