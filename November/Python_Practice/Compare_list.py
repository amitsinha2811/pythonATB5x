# We have defined a fuction which will compare the fisrt and last
# entery of the list and print it as true or false

def first_last_same(numberList):
    print("Given list:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False

number_x = [50,20,30,40,50]
print("result is :", first_last_same(number_x))

number_y = [10,21,31,41,50]
print("result is :",first_last_same(number_y))
