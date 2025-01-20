Data = {"Akku":94,"Bhawna":69,"Deepak":89,"Guru":92,"Sonu":45}
name = input("Enter the student name here:")
if name in Data:
    x= Data[name]
    print(x)
else:
    print("Student data not available here")
print("=========================================")
name1 = input("Enter the student name here:")
if name in Data:
    x= Data.get(name1)
    print(x)
else:
    print("Student data not available here")