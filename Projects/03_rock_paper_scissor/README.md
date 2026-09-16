# 🎮 Rock Paper Scissors

A simple **Rock Paper Scissors** game built using Python.  
The player plays against the computer, which randomly selects rock, paper, or scissor.

## 📌 About the Project

This project was created to practice Python fundamentals and problem-solving skills.

The game allows the user to:

- Choose **Rock**, **Paper**, or **Scissor**
- Play against the computer
- See the computer's randomly selected choice
- Determine the winner
- Play multiple rounds
- Handle invalid user input

## 🛠️ Concepts Used

This project uses the following Python concepts:

- Variables
- Lists
- `while` loop
- `if`, `elif`, and `else`
- `break`
- `continue`
- `input()`
- `print()`
- f-strings
- `random` module
- `random.choice()`
- Membership operator `in` / `not in`
- String methods: `.lower()` and `.strip()`

## 🎯 Game Rules

| Player | Computer | Result |
|---|---|---|
| Rock | Rock | Tie |
| Rock | Paper | Computer wins |
| Rock | Scissor | Player wins |
| Paper | Rock | Player wins |
| Paper | Paper | Tie |
| Paper | Scissor | Computer wins |
| Scissor | Rock | Computer wins |
| Scissor | Paper | Player wins |
| Scissor | Scissor | Tie |

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python rock_paper_scissors.py
```

Or on Windows:

```bash
py rock_paper_scissors.py
```

## 💻 Example

```text
Enter your move: rock, paper, scissor: rock
User choice = rock & Computer choice = scissor
You win! 😍

Do you want to play again (yes/no): no
```

## 📂 Project Structure

```text
03_rock_paper_scissors/
│
├── code.py
└── README.md
```

## 📚 Learning Outcome

Through this project, I practiced Python loops, conditional statements, lists, user input, random selection, input validation, and basic problem-solving.

---

**Built with 🐍 Python**