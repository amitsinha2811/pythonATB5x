string = "Apples are green and sweet"

s = string.split()[::-1]
l = []
for i in s:
    l.append(i)

print(" ".join(l))