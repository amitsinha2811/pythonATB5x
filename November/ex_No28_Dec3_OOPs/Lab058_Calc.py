class Calc:
    def __init__(self):
        print("DC")

    def sum(self ,a,b):
        return a+b
    def sub(self, a,b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b

object_ref = Calc()
a = float(input("Enter the Value of a\n"))
b = float(input("Enter the Value of b\n"))

output_sum = object_ref.sum(a,b)
print(output_sum)
output_sub = object_ref.sub(a,b)
print(output_sub)
output_mul = object_ref.mul(a,b)
print(output_mul)
output_div = object_ref.div(a,b)
print(output_div)