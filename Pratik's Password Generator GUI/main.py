import random
import tkinter as tk
from tkinter import messagebox

Capitals = "QWERTYUIOPASDFGHJKLZXCVBNM"

Smalls = "qwertyuiopasdfghjklzxcvbnm"

Digits = "1234567890"

Symbols = "(){}[],.;':/*-+"


print("Have a happy time generating pasword !!!")

def generate_password():
    all_chars = ""
    if upper_var.get():
        all_chars += Capitals

    if lower_var.get():
        all_chars += Smalls

    if nums_var.get():
        all_chars += Digits

    if syms_var.get():
        all_chars += Symbols

    password_list = []
    for _ in range(amount_var.get()):
        password = "".join(random.sample(all_chars, length_var.get()))
        password_list.append(password)

    result_text.config(state=tk.NORMAL)

    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, "\n".join(password_list))

    result_text.config(state=tk.DISABLED)

    messagebox.showinfo("Info", "Passwords generated successfully!")



window = tk.Tk()
window.title("Pratik's Password Generator GUI")



tk.Label(window, text="Password Options", font=("Comic Sans MS", 20, "bold")).pack()

upper_var = tk.BooleanVar()

lower_var = tk.BooleanVar()

nums_var = tk.BooleanVar()

syms_var = tk.BooleanVar()

tk.Checkbutton(window, text="Uppercase Characters", font=("Comic Sans MS", 12), variable=upper_var, anchor="w", justify="left").pack(fill="x", anchor="w")

tk.Checkbutton(window, text="Lowercase Characters", font=("Comic Sans MS", 12), variable=lower_var, anchor="w", justify="left").pack(fill="x", anchor="w")

tk.Checkbutton(window, text="Digits", font=("Comic Sans MS", 12), variable=nums_var, anchor="w", justify="left").pack(fill="x", anchor="w")

tk.Checkbutton(window, text="Symbols", font=("Comic Sans MS", 12), variable=syms_var, anchor="w", justify="left").pack(fill="x", anchor="w")


tk.Label(window, text="Password Length", font=("Comic Sans MS", 12)).pack()

length_var = tk.IntVar()

length_entry = tk.Entry(window, textvariable=length_var)

length_entry.pack()

tk.Label(window, text="Number of Passwords", font=("Comic Sans MS", 12)).pack()

amount_var = tk.IntVar()

amount_entry = tk.Entry(window, textvariable=amount_var)

amount_entry.pack()

generate_button = tk.Button(window, text="Generate Passwords", font=("Comic Sans MS", 12,), command=generate_password)

generate_button.pack()

result_text = tk.Text(window, height=10, width=40, state=tk.DISABLED)

result_text.pack()

window.mainloop()
