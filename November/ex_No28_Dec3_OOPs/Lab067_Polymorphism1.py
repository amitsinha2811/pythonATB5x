class Mathutils:
    def add(self, a=0, b=0):
        return a+b
    def add(self,a=1,b=1,c=1):
        return a+b+c
    def add(self,a=2,b=2,c=2,d=2):
        return a+b+c+d

math = Mathutils()
op1 = math.add(23,65)
op2 = math.add(2,34,43)
op3 = math.add(23,45,67,78)