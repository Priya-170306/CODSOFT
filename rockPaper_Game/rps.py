import customtkinter as ctk
import random
import winsound

# ------------------ Setup ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Rock Paper Scissors Pro")
app.geometry("450x580")

# ------------------ Variables ------------------
user_score = 0
computer_score = 0
streak = 0
last_user_choice = None

options = ["rock", "paper", "scissors"]

# ------------------ Smart AI ------------------
def smart_computer_choice(user_choice):
    # 60% chance to counter user's last move
    if random.random() < 0.6:
        if user_choice == "rock":
            return "paper"
        elif user_choice == "paper":
            return "scissors"
        elif user_choice == "scissors":
            return "rock"
    return random.choice(options)

# ------------------ Game Logic ------------------
def play(user_choice):
    global user_score, computer_score, streak, last_user_choice

    result_label.configure(text="Thinking... 🤔")
    choice_label.configure(text="")

    # Delay for animation effect
    app.after(800, lambda: show_result(user_choice))


def show_result(user_choice):
    global user_score, computer_score, streak, last_user_choice

    computer_choice = smart_computer_choice(user_choice)

    # Result logic
    if user_choice == computer_choice:
        result = "Tie 🤝"
        streak = 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win 🎉"
        user_score += 1
        streak += 1
        winsound.PlaySound(r"C:\Users\mistry priya\OneDrive\Desktop\CODESOFT\rockPaper_Game\win.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)  
    else:
        result = "You Lose 😢"
        computer_score += 1
        streak = 0
        winsound.PlaySound(r"C:\Users\mistry priya\OneDrive\Desktop\CODESOFT\rockPaper_Game\lose.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    last_user_choice = user_choice

    # Update UI
    choice_label.configure(
        text=f"You: {user_choice.upper()}   |   Computer: {computer_choice.upper()}"
    )
    result_label.configure(text=result)
    score_label.configure(
        text=f"Score → You: {user_score}  |  Computer: {computer_score}"
    )
    streak_label.configure(
        text=f"🔥 Win Streak: {streak}"
    )

# ------------------ Reset ------------------
def reset_game():
    global user_score, computer_score, streak

    user_score = 0
    computer_score = 0
    streak = 0

    choice_label.configure(text="Make your move 👇")
    result_label.configure(text="")
    score_label.configure(text="Score → You: 0  |  Computer: 0")
    streak_label.configure(text="🔥 Win Streak: 0")

# ------------------ UI ------------------

title = ctk.CTkLabel(
    app,
    text="Rock Paper Scissors 🎮",
    font=("Poppins", 24, "bold")
)
title.pack(pady=20)

choice_label = ctk.CTkLabel(
    app,
    text="Make your move 👇",
    font=("Poppins", 14)
)
choice_label.pack(pady=10)

result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Poppins", 18, "bold")
)
result_label.pack(pady=10)

score_label = ctk.CTkLabel(
    app,
    text="Score → You: 0  |  Computer: 0",
    font=("Poppins", 13)
)
score_label.pack(pady=5)

streak_label = ctk.CTkLabel(
    app,
    text="🔥 Win Streak: 0",
    font=("Poppins", 13)
)
streak_label.pack(pady=5)

# Buttons Frame
frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(pady=25)

btn_rock = ctk.CTkButton(
    frame,
    text="🪨 Rock",
    width=130,
    height=45,
    command=lambda: play("rock")
)
btn_rock.grid(row=0, column=0, padx=10, pady=10)

btn_paper = ctk.CTkButton(
    frame,
    text="📄 Paper",
    width=130,
    height=45,
    command=lambda: play("paper")
)
btn_paper.grid(row=0, column=1, padx=10, pady=10)

btn_scissors = ctk.CTkButton(
    frame,
    text="✂️ Scissors",
    width=130,
    height=45,
    command=lambda: play("scissors")
)
btn_scissors.grid(row=1, column=0, columnspan=2, pady=10)

# Reset Button
reset_btn = ctk.CTkButton(
    app,
    text="Reset Game 🔄",
    fg_color="#444",
    hover_color="#666",
    command=reset_game
)
reset_btn.pack(pady=20)

# Footer
footer = ctk.CTkLabel(
    app,
    text="Mini Python Project | RPS Game",
    font=("Poppins", 10)
)
footer.pack(side="bottom", pady=10)

# Run App
app.mainloop()
