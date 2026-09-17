# 🕐 Digital Clock

A simple **Digital Clock** built using Python and Tkinter. The clock displays the current time and date in a graphical window and updates automatically every second.

## 📌 About the Project

This project was created to practice Python GUI development using the built-in **Tkinter** library.

The clock displays:

- Current time
- Current date
- Hours, minutes, and seconds
- AM/PM
- Automatic time updates every second

## 🛠️ Technologies Used

- **Python**
- **Tkinter**
- **time module**

## 📚 Concepts Used

This project helped me practice:

- Importing modules
- Functions
- Variables
- `strftime()`
- Tkinter GUI
- Labels
- Window properties
- `after()` method
- `mainloop()`

## ⚙️ How It Works

1. A Tkinter window is created.
2. A label is created to display the time and date.
3. `strftime()` gets the current time and date.
4. The label is updated with the current information.
5. `after(1000, time)` calls the function again after 1 second.
6. The process continues while the application is running.

### 🔄 Update Flow

```text
Start
  ↓
Create Tkinter Window
  ↓
Create Label
  ↓
Get Current Time & Date
  ↓
Display on Label
  ↓
Wait 1 Second
  ↓
Update Again
  ↓
Repeat
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python digital_clock.py
```

Or on Windows:

```bash
py digital_clock.py
```

## 📂 Project Structure

```text
04_digital_clock/
│
├── code.py
└── README.md
```

## 🖥️ Output

The program opens a graphical window displaying the current time and date.

Example:

```text
21:30:45 PM
09/17/26
```

The displayed values automatically change every second.

## 🎯 Learning Outcome

Through this project, I learned how to create a simple GUI application in Python using Tkinter and how to update information dynamically using the `after()` method.

---

**Built with 🐍 Python and Tkinter**