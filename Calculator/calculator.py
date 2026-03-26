import tkinter as tk

# Custom Calculator Application
# Developed with a unique interface design

current_input = ""

def append_to_input(value):
    global current_input
    current_input += str(value)
    display_var.set(current_input)

def compute_result():
    global current_input
    try:
        result = str(eval(current_input))
        display_var.set(result)
        current_input = result
    except Exception as e:
        display_var.set("Invalid Input")
        current_input = ""

def reset_display():
    global current_input
    current_input = ""
    display_var.set("")

def remove_last_char():
    global current_input
    current_input = current_input[:-1]
    display_var.set(current_input)

# Initialize the main application window
app = tk.Tk()
app.title("Calculator")
app.geometry("320x450")
app.configure(bg="#2e1b4b")
app.resizable(False, False)

display_var = tk.StringVar()

# Create the display entry field
input_display = tk.Entry(
    app,
    textvariable=display_var,
    font=("Helvetica", 24, "bold"),
    bd=12,
    relief=tk.FLAT,
    bg="#4a3c6b",
    fg="#ffffff",
    justify="right",
    insertbackground="#ffffff"
)
input_display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=15)

# Frame for organizing buttons
button_container = tk.Frame(app, bg="#2e1b4b")
button_container.pack()

button_style = ("Helvetica", 14, "bold")

def make_button(label, row_pos, col_pos, action, bg_color="#6b5b95", span=1):
    button = tk.Button(
        button_container,
        text=label,
        width=5 if span == 1 else 12,
        height=2,
        font=button_style,
        bg=bg_color,
        fg="#ffffff",
        bd=0,
        command=action,
        activebackground="#8a7db8",
        relief=tk.RAISED
    )
    button.grid(row=row_pos, column=col_pos, columnspan=span, padx=5, pady=5)

# Define button layout with their properties
button_layout = [
    [("C", 0, 0, reset_display, "#d9534f", 1), ("⌫", 0, 1, remove_last_char, "#f0ad4e", 1), ("%", 0, 2, lambda: append_to_input("%"), "#6b5b95", 1), ("/", 0, 3, lambda: append_to_input("/"), "#6b5b95", 1)],
    [("7", 1, 0, lambda: append_to_input(7), "#6b5b95", 1), ("8", 1, 1, lambda: append_to_input(8), "#6b5b95", 1), ("9", 1, 2, lambda: append_to_input(9), "#6b5b95", 1), ("*", 1, 3, lambda: append_to_input("*"), "#6b5b95", 1)],
    [("4", 2, 0, lambda: append_to_input(4), "#6b5b95", 1), ("5", 2, 1, lambda: append_to_input(5), "#6b5b95", 1), ("6", 2, 2, lambda: append_to_input(6), "#6b5b95", 1), ("-", 2, 3, lambda: append_to_input("-"), "#6b5b95", 1)],
    [("1", 3, 0, lambda: append_to_input(1), "#6b5b95", 1), ("2", 3, 1, lambda: append_to_input(2), "#6b5b95", 1), ("3", 3, 2, lambda: append_to_input(3), "#6b5b95", 1), ("+", 3, 3, lambda: append_to_input("+"), "#6b5b95", 1)],
    [("0", 4, 0, lambda: append_to_input(0), "#6b5b95", 1), (".", 4, 1, lambda: append_to_input("."), "#6b5b95", 1), ("=", 4, 2, compute_result, "#5cb85c", 2)]
]

# Create buttons from the layout
for row in button_layout:
    for btn_info in row:
        make_button(*btn_info)

# Start the GUI event loop
app.mainloop()
