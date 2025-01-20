# accept input starting from a user
word = input("Enter Word : ")
print("Original String:", word)
# get the lenght of a string
size= len(word)
print(len(word))

# iterate a each character of a string
#start : 0 to star with first character
# stop size-1 because start with 0
# step : 2 to get the character present at even index
print("Printing only even index chars")
for i in range(0, size -1,2):
    print(("index[",i,"]", word[i]))
print("======================================")

print("Printing only odd index chars")
for i in range(1, size -1,2):
    print(("index[", i,"]", word[i]))

print("=======================================")
print("Printing only even in reverse index chars")
for i in range(8, 1,-2):
    print(("index[", i,"]", word[i]))
print("======================================")
print("Printing only odd in reverse index chars")
for i in range(9, 0,-2):
    print(("index[", i,"]", word[i]))
