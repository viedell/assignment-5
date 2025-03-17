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
