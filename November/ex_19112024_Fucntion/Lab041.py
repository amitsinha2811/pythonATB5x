pb_global_b = 12 # This is Global variable

def my_function():
    pb_a=10 # this is local variable
    print(pb_a)
    print(pb_global_b)

my_function()

# print(pb_a) This can not be used here as this outside the def block
print(pb_global_b)