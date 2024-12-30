def compute_fectorial(num):
    fectorial=1
    if num<0:
        print(num,"Fectorial of the given number can not be computed ")
    elif num==0:
        print(num, "fectorial of Zero is always 0")
    else:
        for i in range (1, num+1):
            fectorial= fectorial*i
        print("The fectorial of",num,"is",fectorial)

compute_fectorial(int(input("Enter the number :")))