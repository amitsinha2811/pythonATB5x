'''class Calc:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c):
        return a+b+c
    
calc_ref = Calc()
result=calc_ref.sum(3,4)
print(result)''' # If you try to print here you will get Type error

# This will print the value as 8 becoz we have fixed the value of c
'''class Calc:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c

calc_ref = Calc()
result=calc_ref.sum(3,4)
print(result)'''

class Calc:
    def sum(self, *args):
        for a in args:
            print(a)

calc_ref = Calc()
result1=calc_ref.sum(1)
print(result1)
result2=calc_ref.sum(1,2)
print(result2)
result3=calc_ref.sum(1,2,3)
print(result3)
result4=calc_ref.sum(1,2,3,4)
print(result4)
