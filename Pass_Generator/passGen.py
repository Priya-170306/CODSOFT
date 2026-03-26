import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("dark")

# -------- PASSWORD FUNCTION --------
def generate_password():
    name = name_entry.get()
    word = word_entry.get()
    year = year_entry.get()
    length = int(length_slider.get())
    level = level_menu.get()

    if name == "" or word == "" or year == "":
        result_entry.delete(0, "end")
        result_entry.insert(0, "Fill all fields!")
        return

    chars = string.ascii_letters + string.digits + "!@#$%"

    if level == "Easy":
        password = name + word + year
        set_color("#ff6b6b")

    elif level == "Medium":
        password = name[:2] + word[::-1] + year + random.choice(string.digits)
        set_color("#f7b731")

    else:
        password = "".join(random.choice(chars) for _ in range(length))
        set_color("#2ecc71")

    password = password[:length]

    result_entry.delete(0, "end")
    result_entry.insert(0, password)


# -------- COLOR --------
def set_color(c):
    result_entry.configure(border_color=c)


# -------- COPY --------
def copy_password(event):
    app.clipboard_clear()
    app.clipboard_append(result_entry.get())


# -------- THEME SWITCH --------
def toggle_theme():
    global mode
    if mode == "dark":
        ctk.set_appearance_mode("light")
        mode = "light"
        theme_btn.configure(text="☀")
    else:
        ctk.set_appearance_mode("dark")
        mode = "dark"
        theme_btn.configure(text="🌙")


# -------- SLIDER UPDATE --------
def update_length(value):
    length_label.configure(text=f"Length: {int(float(value))}")


# -------- APP --------
app = ctk.CTk()
app.geometry("420x540")   # FIXED SIZE
app.title("SecurePass")

mode = "dark"

# -------- TOP BAR --------
top_frame = ctk.CTkFrame(app, fg_color="transparent")
top_frame.pack(fill="x", pady=5)

theme_btn = ctk.CTkButton(top_frame, text="🌙",
                          width=40, height=40,
                          corner_radius=20,
                          command=toggle_theme)
theme_btn.pack(side="right", padx=10)

# -------- TITLE --------
ctk.CTkLabel(app, text="SecurePass 🔐",
             font=("Arial", 22, "bold")).pack(pady=10)

ctk.CTkLabel(app, text="Create clean & secure passwords",
             font=("Arial", 12)).pack(pady=2)

# -------- INPUTS --------
name_entry = ctk.CTkEntry(app, placeholder_text="Your name", width=280)
name_entry.pack(pady=10)

word_entry = ctk.CTkEntry(app, placeholder_text="Favorite word", width=280)
word_entry.pack(pady=10)

year_entry = ctk.CTkEntry(app, placeholder_text="Birth year", width=280)
year_entry.pack(pady=10)

# -------- LENGTH DISPLAY --------
length_label = ctk.CTkLabel(app, text="Length: 10")
length_label.pack()

length_slider = ctk.CTkSlider(app, from_=4, to=20, command=update_length, width=280)
length_slider.set(10)
length_slider.pack(pady=15)

# -------- STRENGTH --------
level_menu = ctk.CTkOptionMenu(app, values=["Easy", "Medium", "Strong"], width=200)
level_menu.set("Medium")
level_menu.pack(pady=10)

# -------- GENERATE BUTTON --------
ctk.CTkButton(app, text="Generate",
              command=generate_password,
              corner_radius=25,
              width=200).pack(pady=20)

# -------- OUTPUT FRAME (FIXED ALIGNMENT) --------
output_frame = ctk.CTkFrame(app, fg_color="transparent")
output_frame.pack(fill="x", padx=20, pady=10)

result_entry = ctk.CTkEntry(
    output_frame,
    height=35,
    justify="center"
)
result_entry.pack(fill="x")   # IMPORTANT FIX

result_entry.bind("<Double-Button-1>", copy_password)

ctk.CTkLabel(app, text="Double-click to copy",
             font=("Arial", 10)).pack()

app.mainloop()
