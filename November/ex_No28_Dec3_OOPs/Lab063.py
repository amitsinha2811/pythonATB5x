
class Car:
    def __init__(self):
        self.password = "pramod" # public instance variable
        self.__password_secure = "pass123" # private instance variable

    def change_password(self):
        print(self.password)


object_ref = Car()
print(object_ref.password)
print(object_ref.__password_secure) # 'Car' object has no attribute '__password_secure'
