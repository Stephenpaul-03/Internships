import tkinter as tk

bg_color = "#e6e6e6"
btn_color = "#d9d9d9"
clr_btn_color = "#bfbfbf"
eq_btn_color = "#bfbfbf"

root = tk.Tk()
root.title("Calculator")
root.geometry("200x300")
root.configure(bg=bg_color)

entry = tk.Entry(root, font=("Arial", 20), bd=0, highlightthickness=0)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    if text == "C":
        button = tk.Button(root, text=text, font=("Arial", 16), command=clear, bd=0, highlightthickness=0, padx=25, pady=10, bg=clr_btn_color)
    elif text == "=":
        button = tk.Button(root, text=text, font=("Arial", 16), command=calculate, bd=0, highlightthickness=0, padx=25, pady=10, bg=eq_btn_color)
    else:
        button = tk.Button(root, text=text, font=("Arial", 16), command=lambda num=text: button_click(num), bd=0, highlightthickness=0, padx=25, pady=10, bg=btn_color)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
