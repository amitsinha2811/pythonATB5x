#This is first method to update and merge the two dictionary
#dict1 = {"Jhom":89,"Lisa":99}
#dict2 = {"Lisa":94, "peter":83}
#print(dict1 | dict2)

# This is second way to update and merge two dictionary
#dict1 = {"Jhom":89,"Lisa":99}
#dict2 = {"Lisa":94, "peter":83}
#print({**dict1,**dict2})

# This is third method to update and merge the two dictionary
dict1 = {"Jhom":89,"Lisa":99}
dict2 = {"Lisa":94, "peter":83}

dict3 = dict1.copy()
print(dict3.update(dict2))
print(dict3)









