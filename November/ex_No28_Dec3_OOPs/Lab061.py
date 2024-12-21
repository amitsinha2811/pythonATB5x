class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Name of the car is " + self.name)
        print("Make of the car is "+ self.make)
        print("Year of manufecture is " + self.model)

Thar = Car("Thar","3.0 Turbo","2024")
Thar.start_engine()

print("========================================")

Mg_hector= Car("Mg Hector", "2.4 Turbo", "2023")
Mg_hector.start_engine()

