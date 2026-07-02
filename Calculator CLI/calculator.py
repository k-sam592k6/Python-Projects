def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def exponentiate(n1, n2):
    return n1 ** n2


def return_to_menu():
    input("\nPress Enter to return to the Main Menu...")


def result_ui():
    print("\nResult")
    print("----------------------------------------------")


history = []

print("==========================================================")
print("              PYTHON CLI CALCULATOR v1.0")
print("==========================================================")

while True:

    print("\nChoose an Operation")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Exponentiation")
    print("[6] View History")
    print("[7] Clear History")
    print("[8] Exit")

    print("----------------------------------------------------------")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("\nInvalid Input! Please enter a number.")
        return_to_menu()
        continue


    if choice == 1:

        print("\n------------------ ADDITION ------------------")

        try:
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))

            answer = add(a, b)

            history.append(f"{a} + {b} = {answer}")

            result_ui()
            print(f"{a} + {b} = {answer}")

        except ValueError:
            print("Invalid number entered.")

        return_to_menu()


    elif choice == 2:

        print("\n---------------- SUBTRACTION ----------------")

        try:
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))

            answer = subtract(a, b)

            history.append(f"{a} - {b} = {answer}")

            result_ui()
            print(f"{a} - {b} = {answer}")

        except ValueError:
            print("Invalid number entered.")

        return_to_menu()


    elif choice == 3:

        print("\n--------------- MULTIPLICATION ---------------")

        try:
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))

            answer = multiply(a, b)

            history.append(f"{a} × {b} = {answer}")

            result_ui()
            print(f"{a} × {b} = {answer}")

        except ValueError:
            print("Invalid number entered.")

        return_to_menu()


    elif choice == 4:

        print("\n------------------ DIVISION ------------------")

        try:
            a = float(input("Enter numerator   : "))
            b = float(input("Enter denominator : "))

            if b == 0:
                print("\nCannot divide by zero.")
            else:
                answer = divide(a, b)

                history.append(f"{a} / {b} = {answer}")

                result_ui()
                print(f"{a} / {b} = {answer}")

        except ValueError:
            print("Invalid number entered.")

        return_to_menu()


    elif choice == 5:

        print("\n-------------- EXPONENTIATION ----------------")

        try:
            a = float(input("Enter base  : "))
            b = float(input("Enter power : "))

            answer = exponentiate(a, b)

            history.append(f"{a} ^ {b} = {answer}")

            result_ui()
            print(f"{a} ^ {b} = {answer}")

        except ValueError:
            print("Invalid number entered.")

        return_to_menu()


    elif choice == 6:

        print("\n============== CALCULATION HISTORY ==============")

        if len(history) == 0:
            print("No calculations yet.")

        else:
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")

        print("=================================================")

        return_to_menu()


    elif choice == 7:

        history.clear()

        print("\nHistory Cleared Successfully.")

        return_to_menu()


    elif choice == 8:

        print("\nThank you for using Python CLI Calculator.")
        print(f"Total Calculations Performed : {len(history)}")

        break

    else:
        print("\nInvalid Choice!")

        return_to_menu()
