import random


def roll_dice():
    return random.randint(1, 6)


print("===== DICE ROLLER =====")

while True:
    input("Press Enter to roll the dice...")

    result = roll_dice()
    print(f"You rolled: {result}")

    play_again = input("Roll again? (yes/no): ").lower()

    if play_again == "no":
        print("Thanks for playing! 🎲")
        break