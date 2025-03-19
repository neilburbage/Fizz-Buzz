
import random
print("\n")
print("Rock, Paper, Scissor game.\nGame Rules:\n")
print("Rock versus Paper, then Paper wins.\n")
print("Rock versus Scissor, then Rock wins.\n")
print("Paper versus Scissor, then Scissor wins.\n")

while True:
    print("Enter your choice:\n")
    print("1. For Rock.\n2. For Paper.\n3. For Scissor.\n")
    choice = int(input("Enter your choice: \n"))
    while choice > 3 or choice < 1:
        choice = int((input("Enter a valid choice: \n")))

    if choice == 1: 
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    print("User choice is:", choice_name,"\n")
    print("Now it's the computer's turn:\n")
    computer_choice = random.randint(1,3)
    # while computer_choice == choice:
    #     computer_choice = random.randint(1,3)
    
    if computer_choice == 1: 
        computer_name = "Rock"
    elif computer_choice == 2:
        computer_name = "Paper"
    else:
        computer_name = "Scissor"
    print("Computer choice is:", computer_name,"\n")

    print(choice_name," ", "versus", " ",computer_name)
    if choice == computer_choice:
        result = "draw"

    if (choice == 1 and computer_choice == 2):
        print("Paper wins...\n")
        result = "Paper"
    elif (choice == 2 and computer_choice == 1):
        print("Paper wins...\n")
        result = "Paper"

    if (choice == 2 and computer_choice == 3):
        print("Scissor wins...\n")
        result = "Scissor"
    elif (choice == 3 and computer_choice == 2):
        print("Scissor wins...\n")
        result = "Scissor"
    if (choice == 1 and computer_choice == 3):
        print("Rock wins...\n")
        result = "Rock"
    elif (choice == 3 and computer_choice == 1):
        print("Rock wins...\n")
        result = "Rock"
    
    if result == "draw":
        print("It's a tie!\n")
    elif result == choice_name:
        print("User wins\n")
    else:
        print("Computer wins\n")
    
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again == 'n':
        print("Thank you for playing!\nBye bye!")
        break
    else:
        continue
    