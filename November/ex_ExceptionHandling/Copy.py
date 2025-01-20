from shutil import copyfile
#copyfile("C:/Users/hp/PycharmProjects/PythonATB5x/November/ex_ExceptionHandling/Demo.txt","C:/Users/hp/PycharmProjects/PythonATB5x/November/ex_ExceptionHandling/copy.txt")
# f = open("Demo.txt","a")
# f.write("Welcome to python automation\n")
# f.close()
f = open("Demo.txt","a")
t= "We are learning python automation here\n"
for i in range(0,5):
    f.write(t)
f.close()