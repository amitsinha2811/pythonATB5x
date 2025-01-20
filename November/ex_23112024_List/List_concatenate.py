l1 = [13,34,46,67,74,83]
l2= [13,35,46,58,67,74]

# l3= l1+l2
# print(l3)
# l3 = list(set(l1+l2))
# print(l3)
#
# l1.extend(l2)
# print(l1)

res_l4 = []
for i in range (0 , len(l1)):
    res_l4.append(l1[i] + l2[i])
print(res_l4)