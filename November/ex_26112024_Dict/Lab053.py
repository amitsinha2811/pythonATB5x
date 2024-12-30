from queue import PriorityQueue

from November.ex_23112024_Sets.Lab052_Sets import my_set

my_dict = {
    "Name" : "Amit",
    "Age" : 34,
    "Role" : "Tech Lead",
    "Experience" : 9,
}

print(my_dict)
print(my_dict["Age"])
print(my_dict["Role"])

print("=====================================")

my_dict["Role"] = "Automation Lead"
print(my_dict)

print("=======================================")

del my_dict["Age"]
print(my_dict)

print("=====================================")
my_dict["Age"] = 34
print(my_dict)

print("========================================")
for key,value in my_dict.items():
    print(key ,"-->", value)