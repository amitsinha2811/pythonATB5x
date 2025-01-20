# This is program to transpose a matrix using loop

A = [[1,5,8],
     [4,6,7]]
T= [[0,0],
    [0,0],
    [0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i]=A[i][j]
print("The transpose matrix is")
for r in T:
    print(r)

# This is program to transpose a matrix using list comprehension
A = [[1,5,8],
     [4,6,7]]
T = [[A[j][i] for j in range (len(A))] for i in range (len(A[0]))]

print("The transpose matrix is")
for r in T:
    print(r)