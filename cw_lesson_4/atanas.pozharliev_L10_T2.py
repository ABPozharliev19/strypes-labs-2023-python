import tkinter as tk
from tkinter import IntVar, StringVar

window = tk.Tk()
window.geometry("500x300")

word = 'computer'
guessed_chars = []
hidden_word = tk.StringVar(value="_" * len(word))

tries = IntVar(value=6)
won = StringVar()

entry = tk.Entry()
entry.grid()

canvas = tk.Canvas(window)
canvas.create_line(10, 190, 190, 190)
canvas.create_line(50, 190, 50, 20)
canvas.create_line(50, 20, 100, 20)
canvas.create_line(100, 20, 100, 40)
canvas.grid()


def print_hanged_man(num_tries):
    global canvas
    global tries

    num_tries = tries.get()

    if num_tries == 6:
        canvas.create_line(10, 190, 190, 190)
        canvas.create_line(50, 190, 50, 20)
        canvas.create_line(50, 20, 100, 20)
        canvas.create_line(100, 20, 100, 40)
    elif num_tries == 5:
        canvas.create_oval(80, 40, 120, 80)
    elif num_tries == 4:
        canvas.create_line(100, 80, 100, 120)
    elif num_tries == 3:
        canvas.create_line(100, 100, 80, 80)
    elif num_tries == 2:
        canvas.create_line(100, 100, 120, 80)
    elif num_tries == 1:
        canvas.create_line(100, 120, 80, 150)
    elif num_tries == 0:
        canvas.create_line(100, 120, 120, 150)


def update_value():
    global hidden_word
    global word
    global tries
    global won

    new_word = []

    for index, i in enumerate(hidden_word.get()):
        new_word.append(i)

    if entry.get() not in guessed_chars:
        guessed_chars.append(entry.get())

    has_updated = False

    for index, char in enumerate(word):
        if word[index] in guessed_chars:
            new_word[index] = char
            has_updated = True

    try:
        new_word.index("_")
    except ValueError as e:
        won.set("You won")

    if not has_updated:
        tries.set(tries.get() - 1)

        if tries.get() == 0:
            won.set("You lost")

    new_word = "".join(new_word)

    hidden_word.set(new_word)

    entry.delete(0, tk.END)

    print_hanged_man(tries.get())


label = tk.Label(textvariable=hidden_word)
label.grid()

tries_label = tk.Label(textvariable=tries)
tries_label.grid()

win_label = tk.Label(textvariable=won)
win_label.grid()

button = tk.Button(window, text="Guess", command=update_value)
button.grid()

window.mainloop()
