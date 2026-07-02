# Python Quiz Application

A command-line quiz application built in Python that tests knowledge of core Python programming concepts. The application features randomized question ordering, real-time scoring, and session-level statistics tracking, delivered through a structured, menu-driven terminal interface.

## Overview

This project demonstrates the use of core Python data structures and control flow to build an interactive, stateful command-line application. It also served as an exercise in identifying and resolving logic errors in nested loop structures, a common challenge in interactive program design.

## Features

- **10 multiple-choice questions** covering core Python fundamentals (syntax, keywords, data types, and more)
- **Randomized question order** on each playthrough
- **Immediate feedback** on each answer, including the correct answer when a question is missed
- **Real-time score tracking** throughout the quiz
- **Session statistics**, including total quizzes played and highest score achieved
- **Input validation** to handle invalid menu selections and answers without crashing the program
- **Structured menu system** with options to play, view rules, check statistics, or exit

## How It Works

The app runs on a simple loop-driven menu:

```
[1] Start Quiz
[2] Rules
[3] Statistics
[4] Exit
```

Each quiz question presents four options (1–4). Answer correctly to earn a point; the quiz always runs through all 10 questions before showing your final score and percentage.

## Getting Started

### Prerequisites
- Python 3.6

No external dependencies — built entirely with Python's standard library (`random`).

## Project Structure

```
quiz_app.py       # Main application file
├── questions      # Dictionary of quiz questions and answer options
├── answers         # Dictionary mapping question numbers to correct answers
├── main()          # Menu loop and entry point
├── play_game()     # Core quiz logic and scoring
├── show_rules()     # Displays game rules
├── show_stats()      # Displays session statistics
└── display_ques()     # Renders a question and its options
```

## Technical Highlights

- Structured application data using nested dictionaries to represent questions, answer options, and correct answers
- Built an interactive, stateful command-line interface using Python's `input()` function
- Managed control flow across multiple nested loops (menu loop, quiz loop, and per-question answer-validation loop)
- Identified and resolved control-flow defects, including an infinite-loop condition in the answer-validation logic and a premature program termination triggered by invalid menu input, through systematic tracing of program execution

## Possible Future Enhancements

- Add more question categories/topics
- Save high scores to a file so they persist between sessions
- Add a timer per question
- Build a GUI or web version (e.g., with Tkinter or Flask)

## License

This project is open for use and modification for educational and portfolio purposes.
