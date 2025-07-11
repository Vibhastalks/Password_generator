import tkinter as tk
from tkinter import messagebox
import string
import random

# Password generation logic
def generate_password():
    try:
        n_uc = int(uppercase_entry.get())
        n_lc = int(lowercase_entry.get())
        n_sym = int(symbols_entry.get())
        n_num = int(numbers_entry.get())

        password = []
        password += random.choices(string.ascii_uppercase, k=n_uc)
        password += random.choices(string.ascii_lowercase, k=n_lc)
        password += random.choices(string.punctuation, k=n_sym)
        password += random.choices(string.digits, k=n_num)

        random.shuffle(password)
        result = ''.join(password)
        result_var.set(result)

        # Check password strength
        total_len = len(result)
        if total_len < 6:
            strength_var.set("Strength: Weak")
            strength_label.config(fg="red")
        elif total_len < 10:
            strength_var.set("Strength: Medium ")
            strength_label.config(fg="orange")
        else:
            strength_var.set("Strength: Strong")
            strength_label.config(fg="green")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers for all fields.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard! 📋")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x500")
root.configure(bg="#f8f9fa")

title = tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 16, "bold"), bg="#f8f9fa")
title.pack(pady=20)

frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(pady=10)

def create_input(label_text):
    label = tk.Label(frame, text=label_text, font=("Helvetica", 10), bg="#f8f9fa")
    label.pack()
    entry = tk.Entry(frame, font=("Helvetica", 10), width=30)
    entry.pack(pady=5)
    return entry

uppercase_entry = create_input("Number of uppercase letters:")
lowercase_entry = create_input("Number of lowercase letters:")
symbols_entry = create_input("Number of symbols:")
numbers_entry = create_input("Number of digits:")

generate_btn = tk.Button(root, text="Generate Password", font=("Helvetica", 11, "bold"), bg="#4a69bd", fg="white", command=generate_password)
generate_btn.pack(pady=15)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="#333", wraplength=300, pady=10)
result_label.pack(pady=10, padx=20, fill='x')

copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 10), command=copy_to_clipboard, bg="#38a169", fg="white")
copy_btn.pack(pady=5)

strength_var = tk.StringVar()
strength_label = tk.Label(root, textvariable=strength_var, font=("Helvetica", 10, "italic"), bg="#f8f9fa")
strength_label.pack(pady=5)

root.mainloop()
