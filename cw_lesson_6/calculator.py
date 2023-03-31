import tkinter as tk

actions = ["+", "-", "*", "/"]

window = tk.Tk()
window.geometry("600x400")

def handleButtonClick(action):
    global entry
    text = entry.get()

    if action == "+":
        text = entry.get()



entry = tk.Entry()
entry.pack()

window.mainloop()
