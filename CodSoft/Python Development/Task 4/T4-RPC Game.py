import tkinter as tk
from tkinter import ttk
import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def user_choice(user):
    computer = get_computer_choice()
    result = determine_winner(user, computer)
    result_label.config(text=result)
    computer_choice_label.config(text=f"Computer chose: {computer}")
    user_choice_label.config(text="Your choice: " + user)

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x180")  

root.columnconfigure(0, weight=1)  

heading_label_computer = tk.Label(root, text="Computer", font=("Arial", 14))
heading_label_computer.pack(side=tk.TOP)

computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

heading_label_user = tk.Label(root, text="Player", font=("Arial", 14))
heading_label_user.pack()

user_choice_label = tk.Label(root, text="", font=("Arial", 12))
user_choice_label.pack()

style = ttk.Style()
style.configure('TButton', font=('Arial', 10), padding=5)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

rock_button = ttk.Button(button_frame, text="Rock", command=lambda: user_choice("Rock"), style='TButton')
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = ttk.Button(button_frame, text="Paper", command=lambda: user_choice("Paper"), style='TButton')
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = ttk.Button(button_frame, text="Scissors", command=lambda: user_choice("Scissors"), style='TButton')
scissors_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
