A = [[1,5,8],
     [4,6,7],
     [7,2,3]]

B=[[4,5,6],
   [8,9,1],
   [3,5,6]]

Result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
print("The given matrix is",len(A),"x", len(B))
for i in range(len(A)):
    for j in range(len(A[0])):
        Result[i][j]= A[i][j] + B[i][j]
for r in Result:
     print("Sum of given matrix is",r)

print("++++++++++++++++++++++++++++++++++++++++++")
for i in range(len(A)):
    for j in range(len(A[0])):
        Result[i][j]= A[i][j] * B[i][j]
for r in Result:
     print("Multiplication of given matix is",r)
print("+++++++++++++++++++++++++++++++++++++++++++")
for i in range(len(A)):
    for j in range(len(A[0])):
        Result[i][j]= A[i][j] - B[i][j]
for r in Result:
     print("Substraction of given matrix is",r)
print("++++++++++++++++++++++++++++++++++++++++++++++")
for i in range(len(A)):
    for j in range(len(A[0])):
        Result[i][j]= A[i][j] /B[i][j]
for r in Result:
     print("Division of given matrix is",r)
