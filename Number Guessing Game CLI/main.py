import random


def return_to_menu():
    input("\nPress Enter to return to the Main Menu...")


def play_game(difficulty_name, low, high, max_attempts, stats):
    
    secret_number = random.randint(low, high)
    attempts = max_attempts
    tries = 0

    print("====================================================")
    print(f"Difficulty: {difficulty_name}")
    print(f"Guess the number between {low} and {high}")

    stats["games_played"] += 1

    while attempts > 0:
        print(f"Attempts Remaining: {attempts}")
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("\nInvalid input, please enter a whole number.")
            continue

        tries += 1
        attempts -= 1

        if guess == secret_number:
            print("Congratulations!")
            print("You guessed the number correctly!")
            print(f"Secret Number: {secret_number}")
            print(f"Attempts Used: {tries}")

            stats["games_won"] += 1
            if stats["best_score"] is None or tries < stats["best_score"]:
                stats["best_score"] = tries

            return_to_menu()
            return

        elif guess > secret_number:
            print("Too High!")
          
        else:
            print("Too Low!")

    
    print("Game Over!")
    print("You have used all your attempts.")
    print(f"The secret number was: {secret_number}")
    print("Better Luck Next Time!")

    stats["games_lost"] += 1
    return_to_menu()


def show_rules():
    print("==================== GAME RULES ====================")
    print("1. The computer secretly chooses a random number")
    print("2. Your goal is to guess the number")
    print("3. After every guess you'll receive a hint")
    print("Hints:")
    print("Too High \nToo Low \nCorrect!")
    print("Each difficulty gives a limited number of attempts.")
    print("Good Luck!")
    print("====================================================")
    return_to_menu()


def show_stats(stats):
    print("\n================== STATISTICS ==================")
    print(f"Games Played: {stats['games_played']}")
    print(f"Games Won   : {stats['games_won']}")
    print(f"Games Lost  : {stats['games_lost']}")
    print("===============================================")
    return_to_menu()


def main():
    print("==========================================================")
    print("            PYTHON NUMBER GUESSING GAME                   ")
    print("==========================================================")

    stats = {
        "games_played": 0,
        "games_won": 0,
        "games_lost": 0,
    }

    while True:
        print("\nChoose Difficulty: ")
        print("[1] Easy        (10 Attempts | Number 1-50)")
        print("[2] Medium      (7 Attempts  | Number 1-100)")
        print("[3] Hard        (5 Attempts  | Number 1-200)")
        print("[4] Rules")
        print("[5] Stats")
        print("[6] Exit")
        print("----------------------------------------------------------")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input, please enter a number.")
            return_to_menu()
            continue

        if choice == 1:
            play_game("Easy", 1, 50, 10, stats)
        elif choice == 2:
            play_game("Medium", 1, 100, 7, stats)
        elif choice == 3:
            play_game("Hard", 1, 200, 5, stats)
        elif choice == 4:
            show_rules()
        elif choice == 5:
            show_stats(stats)
        elif choice == 6:
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("\nInvalid Choice!")
            return_to_menu()


if __name__ == "__main__":
    main()
