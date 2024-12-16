Player_name = input("Enter Player name\n")
match Player_name:
    case "Sachin":
        print("Sachin is in Playing 11")
    case "Saurav":
        print("saurav is in Playing 11")
    case "Rahul":
        print("Rahul is in Palying 11")
    case "Dhoni":
        print("Dhoni is captain")
    case _:
        print("Player name not in playing 11")