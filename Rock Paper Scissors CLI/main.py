import random

CHOICES = {"1": "Rock", "2": "Paper", "3": "Scissor"}

BEATS = {
    "Rock": "Scissor",
    "Paper": "Rock",
    "Scissor": "Paper",
}


def return_to_menu():
    input("\nPress Enter to return to the main menu...")


def show_rules():
    print("===================== RULES =====================")
    print("1. Rock     defeats   Scissors")
    print("2. Scissors defeats   Paper")
    print("3. Paper    defeats   Rock")
    print("4. Win rounds to increase your score")
    print("===================================================")
    return_to_menu()


def show_stats(stats):
    print("\n================== STATISTICS ==================")
    print(f"Games Played : {stats['games_played']}")
    print(f"Rounds Won   : {stats['games_won']}")
    print(f"Rounds Lost  : {stats['games_lost']}")
    print(f"Rounds Drawn : {stats['draws']}")
    print("===============================================")
    return_to_menu()


def judge_round(player_choice, computer_choice):
    
    if player_choice == computer_choice:
        return "draw"
    elif BEATS[player_choice] == computer_choice:
        return "win"
    else:
        return "lose"


def play_game(stats):
    print("====================================================")
    stats["games_played"] += 1

    session = {"player": 0, "computer": 0, "draws": 0}

    while True:
        guess = input(
            "\n[1] Rock  [2] Paper  [3] Scissor  [4] Quit to menu: "
        ).strip()

        if guess == "4":
            break

        if guess not in CHOICES:
            print("\nInvalid Choice!")
            continue

        player_choice = CHOICES[guess]
        computer_choice = random.choice(list(CHOICES.values()))
        outcome = judge_round(player_choice, computer_choice)

        print(f"You Chose: {player_choice}")
        print(f"Computer Chose: {computer_choice}")

        if outcome == "draw":
            print("Result: Draw!")
            session["draws"] += 1
            stats["draws"] += 1
        elif outcome == "win":
            print("Result: You Win!")
            session["player"] += 1
            stats["games_won"] += 1
        else:
            print("Result: You Lose!")
            session["computer"] += 1
            stats["games_lost"] += 1

        print("-------------------------------------")
        print(
            f"Score -> You: {session['player']}  "
            f"Computer: {session['computer']}  Draws: {session['draws']}"
        )
        print("-------------------------------------")

    return_to_menu()


def main():
    print("==========================================================")
    print("              PYTHON ROCK PAPER SCISSORS                  ")
    print("==========================================================")

    stats = {
        "games_played": 0,
        "games_won": 0,
        "games_lost": 0,
        "draws": 0,
    }

    while True:
        print("\n[1] Play")
        print("[2] Rules")
        print("[3] Stats")
        print("[4] Exit")
        print("----------------------------------------------------------")

        try:
            choice_menu = int(input("Choose an option: "))
        except ValueError:
            print("\nPlease enter a valid number.")
            return_to_menu()
            continue

        if choice_menu == 1:
            play_game(stats)
        elif choice_menu == 2:
            show_rules()
        elif choice_menu == 3:
            show_stats(stats)
        elif choice_menu == 4:
            print("Thanks for playing!")
            break
        else:
            print("\nInvalid Choice!")
            return_to_menu()


if __name__ == "__main__":
    main()
