import tkinter as tk
import string
import random
import pyperclip

def generate_password():
    length = int(length_input.get())

    character_sets = []
    if include_uppercase.get():
        character_sets.append(string.ascii_uppercase)
    if include_lowercase.get():
        character_sets.append(string.ascii_lowercase)
    if include_digits.get():
        character_sets.append(string.digits)
    if include_symbols.get():
        character_sets.append(string.punctuation)

    if len(character_sets) == 0:
        result_text.set("Please select at least one character set.")
    else:
        password = ''.join(random.choice(''.join(character_sets)) for _ in range(length))
        result_text.set(password)

def copy_password():
    generated_password = result_text.get()
    if generated_password:
        pyperclip.copy(generated_password)

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("220x300")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#d9e6f2")
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:", bg="#d9e6f2")
length_label.grid(row=0, column=0, pady=5)

length_input = tk.Entry(frame)
length_input.grid(row=0, column=1, pady=5)

include_uppercase = tk.BooleanVar()
include_uppercase.set(True)
upper_check = tk.Checkbutton(frame, text="Include Uppercase", variable=include_uppercase, bg="#d9e6f2")
upper_check.grid(row=1, column=0, columnspan=2, pady=5)

include_lowercase = tk.BooleanVar()
include_lowercase.set(True)
lower_check = tk.Checkbutton(frame, text="Include Lowercase", variable=include_lowercase, bg="#d9e6f2")
lower_check.grid(row=2, column=0, columnspan=2, pady=5)

include_digits = tk.BooleanVar()
include_digits.set(True)
digits_check = tk.Checkbutton(frame, text="Include Digits", variable=include_digits, bg="#d9e6f2")
digits_check.grid(row=3, column=0, columnspan=2, pady=5)

include_symbols = tk.BooleanVar()
include_symbols.set(True)
symbols_check = tk.Checkbutton(frame, text="Include Symbols", variable=include_symbols, bg="#d9e6f2")
symbols_check.grid(row=4, column=0, columnspan=2, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4a90e2", fg="white")
generate_button.pack(pady=10, ipadx=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, bg="#f0f0f0", font=("Arial", 14), padx=10)
result_label.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password, bg="#4a90e2", fg="white")
copy_button.pack(pady=5, ipadx=10)

root.mainloop()
