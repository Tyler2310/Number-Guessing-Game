import tkinter as tk
from tkinter import messagebox
import random



class Guessing_Game:
    def __init__(self):
        self.root = root #Sets up the main window.
        root.title("Guessing Game")
        self.root.config(bg="#4f97e3")


        self.random_number = random.randint(1, 10) #Generates a number between 1 and 10.
        self.attempts = 0
        self.max_attempts = 5

        self.label = tk.Label(root, text="Guess a number between 1 and 10:", font="Helvetica 18 bold")
        self.label.pack()


        self.entry = tk.Entry(root, justify="center", font="Helvetica 18 bold", relief="solid") #Entry field that the users will use to input guess.
        self.entry.pack()


        self.guess_button = tk.Button(root, text="Submit Guess", font="Helvetica 18 bold", command=self.verify, relief="raised")
        self.guess_button.pack()

        self.error_label = tk.Label(root, font="Helvetica 18 bold")
        self.error_label.place(x=900, y=35)
        self.error_label.config(bg="#4f97e3")


        self.reset_button = tk.Button(root, text="Reset", font="Helvetica 18 bold", command=self.reset_game, relief="raised")
        self.reset_button.pack()

        self.list_box = tk.Listbox(root, justify="center", height=5) #Used to list all the guesses during the current round.
        self.list_box.pack()
        self.list_box.config(font="Helvetica 18 bold", fg="#e02d1d", borderwidth=2, relief="solid")



    def verify(self):
        try:
            guess = int(self.entry.get()) #The guess variable is retrieved from the entry field.
            self.attempts += 1 #Incrementally increases the number of attempts after every input.
            if guess < self.random_number:
                self.entry.delete(0, tk.END)
                self.list_box.insert(tk.END, f"{guess} = Too low")
                self.error_label.config(text="")
            elif guess > self.random_number:
                self.entry.delete(0, tk.END)
                self.list_box.insert(tk.END, f"{guess} = Too high")
                self.error_label.config(text="")

            else:
                self.error_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.", fg="#fce303")
                self.list_box.delete(0, tk.END)


            if self.attempts >= self.max_attempts: #Creates a pop-up after 5 attempts.
                messagebox.showerror("Max Attempts Reached", f"Game over! The number was {self.random_number}.")
                self.reset_game()

        except ValueError: # Raises error when a number is not entered.
                self.error_label.config(font="Helvetica 18 bold", text="Please enter a number.")



    def reset_game(self):
        self.random_number = random.randint(1, 10)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.list_box.delete(0, 5)
        self.error_label.config(text="")





if __name__ == "__main__":
    root = tk.Tk()
    game = Guessing_Game()
    root.mainloop()




