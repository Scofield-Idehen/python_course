
import tkinter as tk
import random


window = tk.Tk()
window.title("Guess the Number!")
window.geometry("300x200")


label = tk.Label(window, text="Guess a number between 1 and 100:")
label.pack()

entry = tk.Entry(window)
entry.pack()

result_label = tk.Label(window, text="")
result_label.pack()

submit_button = tk.Button(window, text="Submit")
submit_button.pack()

new_game_button = tk.Button(window, text="New Game")
new_game_button.pack()


secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    guess = int(entry.get())
    attempts += 1

    if guess < secret_number:
        result_label.config(text="Too low! Try again.")
    elif guess > secret_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"You got it in {attempts} attempts!")

def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="")
    entry.delete(0, tk.END)

submit_button.config(command=check_guess)
new_game_button.config(command=new_game)

window.mainloop()