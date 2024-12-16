import time

def time_decorators(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by func ->" , end_time-start_time)
    return wrapper()

@time_decorators
def test_time_1():
    print("Add a function, and time taken by function1 is :")
    time.sleep(2)

@time_decorators
def test_time_2():
    print("Add a function and time taken by function2 is :")
    time.sleep(5)

@time_decorators
def test_time_3():
    print("Add a function and time taken by function 3 is :")
    time.sleep(10)



