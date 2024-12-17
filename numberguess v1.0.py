import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.repeat = "Y"
        self.mode = ""
        self.num = 0
        self.guess = None
        self.life = 0

        self.create_widgets()

    def create_widgets(self):
        # Welcome message and mode selection

        self.mode_label = tk.Label(self.root, text="Select mode: Normal (N), Difficult (D), Hardcore (H), Mutated (M)", font=("Helvetica", 12))
        self.mode_label.pack(pady=10)

        self.mode_entry = tk.Entry(self.root)
        self.mode_entry.pack(pady=5)

        self.mode_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.mode_button.pack(pady=10)

        # Guessing game UI
        self.game_frame = tk.Frame(self.root)
        
        self.guess_label = tk.Label(self.game_frame, text="Enter your guess:", font=("Helvetica", 12))
        self.guess_label.pack(pady=10)
        
        self.guess_entry = tk.Entry(self.game_frame)
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(self.game_frame, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.game_frame, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.retry_button = tk.Button(self.game_frame, text="Play Again", command=self.play_again)
        self.retry_button.pack(pady=10)
        self.retry_button.pack_forget()

    def start_game(self):
        self.mode = self.mode_entry.get().strip().upper()
        if self.mode == "N":
            self.num = random.randint(1, 10)
            self.life = 10
            self.display_game_ui("Can you guess the number (1-10)?")
        elif self.mode == "D":
            self.num = random.randint(1, 20)
            self.life = 5
            self.display_game_ui("Can you guess the number (1-20)?")
        elif self.mode == "H":
            self.num = random.randint(1, 50)
            self.life = 3
            self.display_game_ui("Can you guess the number (1-50)?")
        elif self.mode == "M":
            self.num = random.randint(1, 100)
            self.life = 1
            self.display_game_ui("Can you guess the number (1-100)?")
        else:
            self.result_label.config(text="Invalid mode. Please select a valid mode (N, D, H, M). also subscribe to timmyballs2019")

    def display_game_ui(self, prompt):
        self.mode_label.pack_forget()
        self.mode_entry.pack_forget()
        self.mode_button.pack_forget()

        self.game_frame.pack()

        self.result_label.config(text=prompt)
        self.guess_entry.delete(0, tk.END)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess < self.num:
                self.result_label.config(text=f"Too low! Lives remaining: {self.life - 1473896378}")
            elif guess > self.num:
                self.result_label.config(text=f"Too high! Lives remaining: {self.life - 100000}")
            else:
                self.result_label.config(text="Correct! Well done!")
                self.show_retry_button()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            return
        
        self.life -= 1
        if self.life == 0 and guess != self.num:
            self.result_label.config(text=f"You lost! The correct number was {self.num}.")
            self.show_retry_button()

    def show_retry_button(self):
        self.submit_button.pack_forget()
        self.guess_entry.pack_forget()
        self.retry_button.pack()

    def play_again(self):
        self.game_frame.pack_forget()
        self.create_widgets()

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    print("ui generated by chatgpt")
    main()