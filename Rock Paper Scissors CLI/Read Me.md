# Python Rock Paper Scissors

A command-line Rock-Paper-Scissors game written in Python. Play against the computer, check the rules if you forget them, and keep track of how you're doing across a session.

## Features

- Play Rock, Paper, or Scissors against a computer opponent that picks at random
- Score updates after every round (you, computer, and draws)
- Session stats: games played, rounds won, rounds lost, rounds drawn
- A rules screen if you need a refresher
- Simple text menu, no external dependencies to install

## Requirements

- Python 3.6+

No external packages needed — it only uses the standard library.

## How to Play

1. Launch the game and choose **Play** from the main menu.
2. Pick Rock, Paper, or Scissor each round.
3. The computer picks randomly — the result (Win / Lose / Draw) is shown immediately.
4. Choose **Quit to menu** at any time to stop playing and return to the main menu.

## Main Menu

```
[1] Play
[2] Rules
[3] Stats
[4] Exit
```

## Rules

```
1. Rock     defeats   Scissors
2. Scissors defeats   Paper
3. Paper    defeats   Rock
```

## Project Structure

```
.
├── rock_paper_scissors.py   # Main game script
└── README.md
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

## License

This project is available under the [MIT License](LICENSE).
