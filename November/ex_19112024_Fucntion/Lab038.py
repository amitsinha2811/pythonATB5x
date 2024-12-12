def sum_of_two(a,b):
    return a+b
result = sum_of_two(5,25)
print(result)

def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2
result = sum_of_two_number_with_default(num1=25, num2=52)
print(result)
result= sum_of_two_number_with_default()
print(result)