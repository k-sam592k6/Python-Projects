# Python CLI Calculator

A simple, menu-driven command-line calculator built in Python. It supports basic arithmetic operations along with exponentiation and a running history of all calculations performed during a session.

## Features

- Addition, Subtraction, Multiplication, Division, Exponentiation
- Calculation history (view all past results in the current session)
- Clear history option
- Input validation with error handling (invalid numbers, division by zero)
- Clean, menu-driven CLI interface

<img width="685" height="653" alt="image" src="https://github.com/user-attachments/assets/f8304bf2-dc37-4504-925b-21dfa98495e1" />


## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository
   ```bash
   git clone https://github.com/your-username/python-cli-calculator.git
   cd python-cli-calculator
   ```

2. Run the calculator
   ```bash
   python calculator.py
   ```

## How It Works

The program runs in a continuous loop, displaying a menu of operations. Based on the user's choice, it:

1. Prompts for the required numbers
2. Performs the selected operation using a dedicated function (`add`, `subtract`, `multiply`, `divide`, `exponentiate`)
3. Logs the result to an in-memory `history` list
4. Displays the formatted result back to the user

Error handling is built in for invalid (non-numeric) inputs and division-by-zero cases, so the program never crashes mid-session.

## Project Structure

```
python-cli-calculator/
│
├── calculator.py       # Main program file
└── README.md            # Project documentation
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Built as a personal Python practice project. Feedback and contributions are welcome!
