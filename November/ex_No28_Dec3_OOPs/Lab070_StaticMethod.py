class O:
    def sum(a,b):
        return a+b
    def sub(self,a,b):
        return a-b


print(O.sum(3,4))
print("================")
obj_O = O()
result= obj_O.sub(3,4)
print(result)
