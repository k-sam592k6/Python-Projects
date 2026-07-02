# 🎯 Python Number Guessing Game

A simple command-line number guessing game written in Python. Pick a difficulty, guess the secret number within a limited number of attempts, and track your stats across rounds.

## Features

- Three difficulty levels with different ranges and attempt limits
- Hints after every guess (`Too High` / `Too Low`)
- Persistent session stats: games played, won, lost, and your best score (fewest attempts used in a win)
- Simple menu-driven interface, no external dependencies

## Difficulty Levels

| Difficulty | Range   | Attempts |
|------------|---------|----------|
| Easy       | 1–50    | 10       |
| Medium     | 1–100   | 7        |
| Hard       | 1–200   | 5        |

## Requirements

- Python 3.6+

No external packages needed — it only uses the standard library.

## How to Play

1. Launch the game and choose an option from the main menu.
2. Pick a difficulty (Easy, Medium, or Hard).
3. Enter your guess when prompted.
4. Use the `Too High` / `Too Low` hints to narrow down the number.
5. Guess correctly before you run out of attempts to win!

## Main Menu

```
[1] Easy        (10 Attempts | Number 1-50)
[2] Medium      (7 Attempts  | Number 1-100)
[3] Hard        (5 Attempts  | Number 1-200)
[4] Rules
[5] Stats
[6] Exit
```

## Project Structure

```
.
├── number_guessing_game.py   # Main game script
└── README.md
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

## License

This project is available under the [MIT License](LICENSE).
