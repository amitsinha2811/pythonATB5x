class Father:
    key = "2BHK"

    def car(self):
        print("Father has a car => Alto")
        print(self.key)
class Son(Father):
    key2 = "3BHK"
    def suv(self):
        print("Son has a Car => Kia")
        print(self.key2)

Father_obj = Father()
Father_obj.car()

Son_obj = Son()
Son_obj.suv()
Son_obj.key2
Son_obj.key
Son_obj.car()
