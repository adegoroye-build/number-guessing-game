import tkinter as tk
from tkinter import ttk
import random
import winsound  # For sound effects (Windows only)

# Function to play sound


def play_sound(sound_type):
    if sound_type == "correct":
        winsound.Beep(800, 300)  # High beep (freq=800Hz, duration=300ms)
    elif sound_type == "wrong":
        winsound.Beep(400, 200)  # Low beep
    elif sound_type == "gameover":
        winsound.Beep(200, 600)  # Deep long beep

# Function to check guess


def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="⚠️ Please enter a number!", fg="orange")
        return

    attempts += 1
    progress["value"] = attempts

    if guess < secret_number:
        result_label.config(text="Too low! ❌", fg="red")
        play_sound("wrong")
    elif guess > secret_number:
        result_label.config(text="Too high! ❌", fg="red")
        play_sound("wrong")
    else:
        result_label.config(
            text=f"🎉 Correct! It was {secret_number}. You guessed in {attempts} tries.",
            fg="green"
        )
        play_sound("correct")
        guess_button.config(state="disabled")
        replay_button.config(state="normal")
        return

    if attempts >= 10:
        result_label.config(
            text=f"💀 Game Over! The number was {secret_number}.",
            fg="black"
        )
        play_sound("gameover")
        guess_button.config(state="disabled")
        replay_button.config(state="normal")

# Function to reset the game


def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(
        text="Game reset! Guess a number between 1 and 100.", fg="blue")
    entry.delete(0, tk.END)
    guess_button.config(state="normal")
    replay_button.config(state="disabled")
    progress["value"] = 0


# Setup window
root = tk.Tk()
root.title("Guessing Game with Sounds 🎵")
root.geometry("420x350")

secret_number = random.randint(1, 100)
attempts = 0

# Widgets
title_label = tk.Label(
    root, text="🎯 Guess a number between 1 and 100", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

guess_button = tk.Button(
    root, text="Guess", command=check_guess, font=("Arial", 12))
guess_button.pack(pady=5)

replay_button = tk.Button(root, text="Play Again", command=reset_game, font=(
    "Arial", 12), state="disabled")
replay_button.pack(pady=5)

result_label = tk.Label(root, text="Start guessing...",
                        font=("Arial", 11), fg="blue")
result_label.pack(pady=10)

progress = ttk.Progressbar(root, length=300, maximum=10, mode="determinate")
progress.pack(pady=10)

note_label = tk.Label(root, text="⚡ You have max 10 tries!",
                      font=("Arial", 10, "italic"))
note_label.pack()

root.mainloop()
