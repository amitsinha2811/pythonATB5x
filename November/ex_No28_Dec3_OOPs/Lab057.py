class Person:
    def __init__(self):
        print("I will be called")
        self.name = input("Enter the name\n")
        self.age = input("Enter your age\n")
        self.phone = input("Enter your phone No \n")
        self.occupation = input("Enter the Occupation \n")
    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}", f"age is {self.age}", f"Phone No is {self.phone}","and", f"occupation is {self.occupation}")

person1 = Person()
person1.name_of_the_function_to_display()

