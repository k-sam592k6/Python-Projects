import random

questions = {
    
    1 : {
        "Question" : "Who developed Python Programming Language?",
        "Options" : {
            "1" : "Wick van Rossum",
            "2" : "Rasmus Lerdorf",
            "3" : "Guido van Rossum",
            "4" : "Niene Stom"
        }
    },
    
    2 : {
        "Question" : "Which type of Programming does Python support",
        "Options" : {
            "1" : "object-oriented programming",
            "2" : "structured programming",
            "3" : "functional programming",
            "4" : "all of the mentioned"
        }
    },
    
    3 : {
        "Question" : "Is Python case sensitive when dealing with identifiers?",
        "Options" : {
            "1" : "no",
            "2" : "yes",
            "3" : "machine dependent",
            "4" : "none of the mentioned"
        }
    },
    
    4 : {
        "Question" : "Which of following is the correct extension of the Python file?",
        "Options" : {
            "1" : ".python",
            "2" : ".pl",
            "3" : ".py",
            "4" : ".p"
        }
    },
    
    5 : {
        "Question" : "Is Python code compiled or interpreted?",
        
        "Options" : {
            "1" : "Python code is both compiled and interpreted",
            "2" : "Python code is neither compiled nor interpreted",
            "3" : "Python code is only compiled",
            "4" : "Python code is only interpreted"
        }
    },
    
    6 : {
        "Question" : "All keywords in Python are in",
        "Options" : {
            "1" : "Capitalized",
            "2" : "lower case",
            "3" : "UPPER CASE",
            "4" : "None of the mentioned"
        }
    },
    
    7 : {
        "Question" : "What will be the value of the following Python expression?  \nprint(4 + 3 % 5)",
        
        "Options" : {
            "1" : "7",
            "2" : "2",
            "3" : "4",
            "4" : "1"
        }
    },
    
    8 : {
        "Question" : "Which of the following is used to define a block of code in Python langauage?",
        
        "Options" : {
            "1" : "Indentation",
            "2" : "Key",
            "3" : "Brackets",
            "4" : "All of the mentioned"
        }
    },
    
    9 : {
        "Question" : "Which keyword is used for function in Python langauage?",
        
        "Options" : {
            "1" : "Function",
            "2" : "def",
            "3" : "Fun",
            "4" : "Define"
        }
    },
    
    10 : {
        "Question" : "Which of the following character is used to give single-line comments in Python?",
        
        "Options" : {
            "1" : "//",
            "2" : "#",
            "3" : "!",
            "4" : "/*"
        }
    }
}

answers = {
    1 : "3",
    2 : "4",
    3 : "2",
    4 : "3",
    5 : "1",
    6 : "4",
    7 : "1",
    8 : "1",
    9 : "2",
    10 : "2"
}

def display_ques(a):
    quiz = questions[a]
    opts = quiz["Options"]
    
    print("Question:", quiz["Question"])
    print("\nOptions:")
    print("1.", opts["1"])
    print("2.", opts["2"])
    print("3.", opts["3"])
    print("4.", opts["4"])

def main():
    
    stats = {
        "quizes_played" : 0,
        "highest_score" : 0
    }
    
    print("==========================================================")
    print("              PYTHON QUIZ APPLICATION                     ")
    print("==========================================================")
    
    while True:
        print("Chose an Option")
        print("[1] Start Quiz \n[2] Rules \n[3] Statistics \n[4] Exit")
    
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("\nInvalid Choice!")
            return_to_menu()
            # BUGFIX: was `return`, which quit the whole program on any
            # non-numeric input. Now it just loops back to the menu.
            continue
        
        if choice == 1:
            play_game(stats)
        elif choice == 2:
            show_rules()
        elif choice == 3 :
            show_stats(stats)
        elif choice == 4:
            print("Thanks for Playing!")
            break
        else:
            print("\nInvalid Choice!")
            return_to_menu()
        
def show_rules():
    
    print("===================== RULES =====================")
    
    print("1. Each question has four options")
    
    print("2. Only one option is correct")
    
    print("3. Every correct answer gives 1 point")
    
    print("4. No negartive marking")
    
    print("5. Final score will be displayed after the quiz")
    
    print("=================================================")
    
    return_to_menu()
    
def play_game(stats):
    
    stats['quizes_played'] += 1
    
    score = 0
        
    question_numbers = list(questions.keys())
    random.shuffle(question_numbers)

    for q in question_numbers:
            
        display_ques(q)
        while True:
            guess = input("Enter your answer:")

            # BUGFIX: previously, a *correct* or *wrong-but-valid* answer
            # never broke out of this loop (so the same question repeated
            # forever), while an *invalid* entry was the only thing that
            # broke out (silently skipping the question). The branches
            # below now break in the right places: correct/wrong answers
            # move on to the next question, invalid input re-prompts.

            if guess == answers[q]:
                score += 1
                print("Correct Answer!")
                print(f"Current Score: {score}")
                break

            elif guess not in ['1', '2', '3', '4']:
                print("\nInvalid Choice! Please enter 1, 2, 3, or 4.")
                continue

            else:
                print("Wrong Answer!")
                print(questions[q]["Options"][answers[q]])
                print(f"Current Score : {score}")
                break
    
    print("==================================================")
    print("Quiz Completed!")
    print(f"Score : {score}/10")
    print(f"Percentage : {score * 10}%")
    print("==================================================")
    
    if score > stats['highest_score']:
        stats['highest_score'] = score
    else:
        pass
    
    return_to_menu()
    
    
def show_stats(stats):
    
    print("\n================== STATISTICS ==================")
    
    print(f"Quizes Played : {stats['quizes_played']}")
    
    print(f"Highest Score : {stats['highest_score']}")
    
    return_to_menu()
    

def return_to_menu():
    input("\nPress Enter to reach Main Menu")


if __name__ == "__main__":
    main()
