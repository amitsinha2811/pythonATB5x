 # set is collection of unique items and represented by {}

my_set = {1,2,2,3,3,4,5,5}
print(my_set)
print(my_set)
print(my_set)

print("========================")

set_1= {1,2,3}
set_2= {4,5,6}
set_3= set_1.union(set_2)
print(set_3)

print("=========================")

set_4={1,2,3,4,5}
set_5={4,5,6,7,8}
set_6=set_4.intersection(set_5)
print(set_6)

print("============================")

set_7=set_4.difference(set_5)
print(set_7)
print("=============================")
set_8=set_5.difference(set_4)
print(set_8)