score= int(input("Enter the marks obtained :\n"))
if score > 90 and score <=100:
    print("Congratulation you have got Grade A")
elif score > 80 and score <=89:
    print("Congratulation You have obtained Grade B")
elif score >70 and score <= 79:
    print("You have obtained Grade C")
elif score > 60 and score <= 69:
    print("You have obtained Grade D")
elif score >0 and score <=59:
    print("Failed, Your Grade is F")
else :
    print("Please Enter a valid Score")