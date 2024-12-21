a=10

class Person:
    b=11 # This is called instance variable
    def print_info(self):
        c=20 # this is called local variable
        print(c)
        print(self.b)
        #a="Hello"
        #print(a) #Hello will be printed as local variable has higher preference than global
        global a
        print(a)


object_ref = Person()
object_ref.print_info()