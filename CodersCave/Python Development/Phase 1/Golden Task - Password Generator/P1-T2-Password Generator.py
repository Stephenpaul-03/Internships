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
root.title("Password Generator")
root.geometry("250x325")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:", bg="#f0f0f0")
length_label.grid(row=0, column=0, pady=5)

length_input = tk.Entry(frame)
length_input.grid(row=0, column=1, pady=5)

include_uppercase = tk.BooleanVar()
include_uppercase.set(True)
upper_check = tk.Checkbutton(frame, text="Include Uppercase", variable=include_uppercase, bg="#f0f0f0")
upper_check.grid(row=1, column=0, columnspan=2, pady=5)

include_lowercase = tk.BooleanVar()
include_lowercase.set(True)
lower_check = tk.Checkbutton(frame, text="Include Lowercase", variable=include_lowercase, bg="#f0f0f0")
lower_check.grid(row=2, column=0, columnspan=2, pady=5)

include_digits = tk.BooleanVar()
include_digits.set(True)
digits_check = tk.Checkbutton(frame, text="Include Digits", variable=include_digits, bg="#f0f0f0")
digits_check.grid(row=3, column=0, columnspan=2, pady=5)

include_symbols = tk.BooleanVar()
include_symbols.set(True)
symbols_check = tk.Checkbutton(frame, text="Include Symbols", variable=include_symbols, bg="#f0f0f0")
symbols_check.grid(row=4, column=0, columnspan=2, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#7fb3d5")
generate_button.pack(pady=10, ipadx=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, bg="#f0f0f0", font=("Helvetica", 14), padx=10)
result_label.pack()

copy_button = tk.Button(root, text="Copy Generated Password", command=copy_password, bg="#7fb3d5")
copy_button.pack(pady=5, ipadx=10)

root.mainloop()
