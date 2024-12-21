class VWOLoginPage:
    def __init__(self,email_args, password_args):
        self.email = email_args
        self.password = password_args

    def login_check(self):
        if self.email=="amit.sinha@gmail.com" and self.password == "PataNahi":
            print("Login Successful")
        else:
            print("Please check your credential")

email = input("Enter your Email \n")
password = input("Enter your password \n")

vwo_obj = VWOLoginPage(email,password)
vwo_obj.login_check()
