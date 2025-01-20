# Python code to print longest consecutive list.

# Input list initialization
Input = [12, 13, 14, 17, 18, 23, 24, 25, 25, 26, 27]

# Output list initialization
Output = []
temp = []
last = -1

# Iteration
for elem in Input:
    if elem - last == 1:
        temp.append(last)
    else:
        temp.append(last)
        Output.append(temp)
        temp = []
    last = elem

ans = []
most = 0

for elem in Output:
    if len(elem) > most:
        most = len(elem)
        ans = elem

# Printing output
print("Initial List is")
print(Input)
print("Longest Consecutive list is :")
print(ans)
