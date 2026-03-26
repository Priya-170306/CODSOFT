# 🎮 Rock Paper Scissors Game (Python GUI)

## 📌 About This Project

This is a Rock Paper Scissors game that I built using Python.
Instead of making a simple console version, I tried to create a proper GUI-based application with a better user experience.

The main idea was to practice:

* GUI development
* Game logic
* User interaction

---

## 🚀 Features

* Play against computer
* Shows both user and computer choices
* Displays result (Win / Lose / Tie)
* Score tracking system
* Win streak counter
* Reset button
* Small delay animation (Thinking effect)
* Sound effects on win and loss

---

## 🛠️ Technologies Used

* Python
* CustomTkinter (for GUI design)
* Random module (to generate computer moves)
* Winsound / Pygame (for sound effects)

---

## ▶️ How to Run the Project

1. Install required libraries:

```id="run1"
pip install customtkinter
```

(If using pygame for sound)

```id="run2"
pip install pygame
```

2. Run the file:

```id="run3"
python rps_game.py
```

---

## 📁 Files in This Project

```id="files1"
rps_game.py   → Main application code  
win.wav       → Sound when user wins  
lose.wav      → Sound when user loses  
README.md     → Project documentation  
```

---

## 🧠 Explanation of Code (Step-by-Step)

### 1. Importing Libraries

```python id="code1"
import customtkinter as ctk
import random
import winsound
```

* `customtkinter` → Used to create modern GUI
* `random` → Helps computer choose randomly
* `winsound` → Plays sound effects

---

### 2. Setting Up Window

```python id="code2"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
```

* Dark mode is enabled
* Blue theme is applied

```python id="code3"
app = ctk.CTk()
app.title("Rock Paper Scissors Pro")
app.geometry("450x580")
```

* Creates main window
* Sets title and size

---

### 3. Variables Used

```python id="code4"
user_score = 0
computer_score = 0
streak = 0
```

* Keeps track of scores and win streak

```python id="code5"
options = ["rock", "paper", "scissors"]
```

* List of possible choices

---

### 4. Smart Computer Logic

```python id="code6"
def smart_computer_choice(user_choice):
```

* This function decides computer move

* 60% chance:

  * Computer tries to beat user

* Otherwise:

  * Picks randomly

---

### 5. Play Function

```python id="code7"
def play(user_choice):
```

* Runs when user clicks a button
* Shows “Thinking...” text
* Calls result function after delay

```python id="code8"
app.after(800, lambda: show_result(user_choice))
```

* Adds delay (animation feel)

---

### 6. Result Logic

```python id="code9"
def show_result(user_choice):
```

* Compares user and computer choice

Cases:

* Same → Tie
* Winning condition → User wins
* Else → User loses

---

### 7. Score and Streak Update

```python id="code10"
user_score += 1
streak += 1
```

* Updates when user wins

```python id="code11"
streak = 0
```

* Resets on loss or tie

---

### 8. Sound Effects

```python id="code12"
winsound.PlaySound("win.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
```

* Plays win sound

```python id="code13"
winsound.PlaySound("lose.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
```

* Plays lose sound

---

### 9. Reset Function

```python id="code14"
def reset_game():
```

* Resets score
* Resets streak
* Updates UI

---

### 10. UI Components

* Labels → Show text (result, score, choices)
* Buttons → User input (Rock, Paper, Scissors)
* Frame → Organizes buttons

---

### 11. Main Loop

```python id="code15"
app.mainloop()
```

* Keeps the app running

---

## 🎯 How the Game Works (Simple Flow)

1. User clicks a button
2. App shows “Thinking...”
3. Computer selects move
4. Result is calculated
5. Score & streak updated
6. Sound plays
7. UI updates

---

## 💡 What I Learned

* Creating GUI using Python
* Handling button events
* Writing game logic
* Improving user experience
* Adding sound effects

---

## 🔮 Future Improvements

* Add difficulty levels
* Add background music
* Store scores permanently
* Convert to executable (.exe)

---

## 👨‍💻 Author

This project was created as part of my practice and internship preparation to improve my Python and GUI development skills.
Priya Mistry
