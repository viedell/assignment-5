import random
choices = ["rock", "paper", "scissors"]
user_score, comp_score = 0, 0
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice == "exit":
        break
    if user_choice not in choices:
        print("Invalid choice, try again.")
        continue
    comp_choice = random.choice(choices)
    print("Computer chose:", comp_choice)
    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1
    print("Score - You:", user_score, "Computer:", comp_score)

if __name__ == "__main__":
    print("Choose a problem (1-10):")
    choice = int(input())
    if choice == 1:
        check_number()
    elif choice == 2:
        even_or_odd()
    elif choice == 3:
        grade_score()
    elif choice == 4:
        largest_number()
    elif choice == 5:
        leap_year()
    elif choice == 6:
        calculator()
    elif choice == 7:
        bmi_calculator()
    elif choice == 8:
        triangle_type()
    elif choice == 9:
        login_system()
    elif choice == 10:
        rock_paper_scissors()
    else:
        print("Invalid choice")
