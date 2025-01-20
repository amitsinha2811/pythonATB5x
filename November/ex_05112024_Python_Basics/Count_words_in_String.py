# def freq_words():
#     str = input("Enter the string here:")
#     li= str.split()
#     d = { }
#     for i  in li:
#         if i not in d.keys():
#             d[i]=0
#         d[i]= d[i]+1
#     print(d)
# freq_words()

# list1= ['Naina','Kimi','Sheena']
# list2= [7678,6454,8763]
#
# list1.extend(list2)
# print(list1)

list1= ['Naina','Kimi','Sheena']
list2= [7678,6454,8763]
data = zip(list1,list2)
print(dict(data))