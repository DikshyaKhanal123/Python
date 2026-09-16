import random

item_list = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Enter your move: rock, paper, scissor: ")

    if user_choice not in item_list:
        print("Invalid input!")
        continue

    cmp_choice = random.choice(item_list)

    print(f"User choice = {user_choice} & Computer choice = {cmp_choice}")

    if cmp_choice == user_choice:
        print("Tie 🥲🥲")

    elif cmp_choice == "rock":
        if user_choice == "scissor":
            print("Computer win! 🥲")
        else:
            print("You win! 😍")

    elif cmp_choice == "paper":
        if user_choice == "scissor":
            print("You win! 😍")
        else:
            print("Computer win! 🥲")

    elif cmp_choice == "scissor":
        if user_choice == "paper":
            print("Computer win! 🥲")
        else:
            print("You win! 😍")

    play_again = input("Do you want to play again (yes/no): ")

    if play_again == "no":
        break