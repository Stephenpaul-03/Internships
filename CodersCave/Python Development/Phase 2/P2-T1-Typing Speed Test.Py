import tkinter as tk
import random
import time

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("600x300")

        self.quote_label = tk.Label(self.root, text="", font=('Arial', 12), wraplength=500)
        self.quote_label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=('Arial', 12), width=100)
        self.entry.pack(padx=20, pady=20)

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=('Arial', 12))
        self.result_label.pack(pady=20)

    def get_random_quote(self):
        quotes = [
            "The cake is a lie.",
            "Nothing is true, everything is permitted.",
            "Did I ever tell you what the definition of insanity is? Insanity is doing the exact same thing over and over again, expecting things to change. That is crazy.",
            "On your feet, soldier. We are leaving!",
            "Bravo Six, going dark.",
            "The numbers, Mason! What do they mean?",
            "Close your heart to their desperation. Close your heart to their suffering. Do not allow yourself to feel for them. They will not feel for you.",
        ]
        return random.choice(quotes)

    def calculate_speed(self, start_time, end_time, typed_text):
        words_typed = len(typed_text.split())
        time_taken = end_time - start_time
        minutes = time_taken / 60
        speed = words_typed / minutes if minutes > 0 else 0
        return speed

    def start_typing_test(self):
        self.quote_label.config(text=self.get_random_quote())
        self.start_time = time.time()

        self.entry.delete(0, tk.END)
        self.entry.focus()

        self.start_button.config(state=tk.DISABLED)
        self.entry.bind('<Return>', self.end_typing_test)

    def end_typing_test(self, event):
        end_time = time.time()
        typed_text = self.entry.get()

        speed = self.calculate_speed(self.start_time, end_time, typed_text)
        self.result_label.config(text=f"Your typing speed: {speed:.2f} words per minute")

        self.start_button.config(state=tk.NORMAL)
        self.entry.unbind('<Return>')

def main():
    root = tk.Tk()
    typing_speed_tester = TypingSpeedTester(root)
    root.mainloop()

if __name__ == "__main__":
    main()
