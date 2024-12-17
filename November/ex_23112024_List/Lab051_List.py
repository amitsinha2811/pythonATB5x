# List is a collection of data
# List can store homogenious as well as hetrogenious data types
# Duplication is allowed in list

my_list1 = [1,2,3,4]
my_list2 = [1,2.9,"Amit", True]

print(my_list1)
print(len(my_list1))
print(my_list2)
print(len(my_list2))

print("===============================")
my_list1.append(9)
print(my_list1)

print("================================")
my_list2.append("Ashmit")
print(my_list2)

print("================================")
my_list1.extend(my_list2)
print(my_list1)


print("----------------")
for i in my_list1:
    print(i)

print("-----------------")
for item in my_list2:
    print(item)