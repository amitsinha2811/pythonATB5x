nterms = int(input("Enter number of terms here :"))

result = list(map(lambda x : 2** x, range(nterms+1)))
print(result)
for i in range(nterms+1):
    print("The value of 2 raised to to power", i,"is",result[i])