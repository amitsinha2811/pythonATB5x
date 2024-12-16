def add_extra_security(func):

    def wrapper():
        print("1. Before the function is called.")
        print("2. Add Helmet, Dashcash,gloves, knee guard, license")
        func()
        print("After function is called")
        print("Leave all the items for next secured drive ")
    return wrapper()

@add_extra_security
def driving_scooty():
    print("Normal function")
    print("I am driving the scooty")