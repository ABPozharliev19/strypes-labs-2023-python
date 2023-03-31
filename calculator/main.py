import re
import math
import tkinter as tk
from tkinter import StringVar

window = tk.Tk()
window.geometry("600x800")
window.resizable = False
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame = tk.Frame(window)

current = StringVar()
previous = StringVar()
memory = StringVar()
last_action = StringVar()
main_input = tk.Entry(
    textvariable=current,
    width=30,
    font=("", 20),
    justify="right",
    state=tk.DISABLED
)
main_input.grid(pady=10)


def on_click_button_number(button_clicked: int):
    global current
    global main_input
    global last_action

    current_number = current.get()

    if last_action.get() != "" and len(re.findall(r"\+|-|\*|/", current_number)) != 0:
        current.set(str(button_clicked))
        return

    if len(current_number) == 0 and button_clicked == 0:
        return

    current.set(current_number + str(button_clicked))


def on_click_dot():
    global current

    current.set(current.get() + ".")


def on_click_action(action: str):
    global last_action
    global current
    global previous

    last_action.set(action)

    previous.set(current.get())
    current.set(action)


def on_click_enter():
    global previous
    global current
    global last_action

    previous_number = previous.get()
    current_number = current.get()
    last = last_action.get()

    if previous_number == "" or current_number == "" or len(re.findall(r"\+|-|\*|/", current_number)) != 0 or last == "":
        return

    last_action.set("")
    previous.set("")

    if last == "+":
        answer = float(previous_number) + float(current_number)
    elif last == "-":
        answer = float(previous_number) - float(current_number)
    elif last == "*":
        answer = float(previous_number) * float(current_number)
    else:
        if current_number == "0":
            current.set("0")
            return
        else:
            answer = float(previous_number) / float(current_number)

    current.set(str(answer))


def on_click_change_sign():
    global current

    current.set(str(-1 * float(current.get())))


def on_click_sqrt():
    global current

    current.set(str(math.sqrt(float(current.get()))))


def on_memory_click(action: str):
    global memory
    global current
    global previous
    global last_action

    current_number = current.get()
    if current_number == "":
        current_number = 0

    previous_number = previous.get()
    if previous_number == "":
        previous_number = 0

    current_memory = memory.get()
    if current_memory == "":
        current_memory = 0

    if action == "clear":
        memory.set("")
    elif action == "read":
        current.set(current_memory)

        if len(re.findall(r"\+|-|\*|/", current.get())) != 0:
            previous.set("")
            last_action.set("")
    elif action == "store":
        if len(re.findall(r"\+|-|\*|/", current.get())) != 0:
            last_action.set("")
            current.set("")
            memory.set(previous_number)
        else:
            memory.set(current_number)
    elif action == "plus":
        if len(re.findall(r"\+|-|\*|/", current.get())) != 0:
            last_action.set("")
            current.set("")
            memory.set(
                str(float(current_memory) + float(previous_number))
            )
        else:
            memory.set(
                str(float(current_memory) + float(current_number))
            )
    else:
        if len(re.findall(r"\+|-|\*|/", current.get())) != 0:
            last_action.set("")
            current.set("")
            memory.set(
                str(float(current_memory) - float(previous_number))
            )
        else:
            memory.set(
                str(float(current_memory) - float(current_number))
            )


mc = tk.Button(frame, text="MC", command=lambda: on_memory_click("clear"))
mplus = tk.Button(frame, text="M+", command=lambda: on_memory_click("plus"))
mminus = tk.Button(frame, text="M-", command=lambda: on_memory_click("minus"))
mr = tk.Button(frame, text="MR", command=lambda: on_memory_click("read"))
ms = tk.Button(frame, text="MS", command=lambda: on_memory_click("store"))

ce = tk.Button(frame, text="CE", command=lambda: on_memory_click("clear"))
ac = tk.Button(frame, text="AC", command=lambda: on_memory_click("clear"))

dot = tk.Button(frame, text=".", command=on_click_dot)

sqrt = tk.Button(frame, text="sqrt", command=on_click_sqrt)

change_sign = tk.Button(frame, text="-x", command=on_click_change_sign)

button_plus = tk.Button(frame, text="+", command=lambda: on_click_action("+"))
button_minus = tk.Button(frame, text="-", command=lambda: on_click_action("-"))
button_multiplication = tk.Button(frame, text="*", command=lambda: on_click_action("*"))
button_division = tk.Button(frame, text="/", command=lambda: on_click_action("/"))

enter = tk.Button(frame, text="=", command=on_click_enter)

button_1 = tk.Button(frame, text="1", command=lambda: on_click_button_number(1))
button_2 = tk.Button(frame, text="2", command=lambda: on_click_button_number(2))
button_3 = tk.Button(frame, text="3", command=lambda: on_click_button_number(3))
button_4 = tk.Button(frame, text="4", command=lambda: on_click_button_number(4))
button_5 = tk.Button(frame, text="5", command=lambda: on_click_button_number(5))
button_6 = tk.Button(frame, text="6", command=lambda: on_click_button_number(6))
button_7 = tk.Button(frame, text="7", command=lambda: on_click_button_number(7))
button_8 = tk.Button(frame, text="8", command=lambda: on_click_button_number(8))
button_9 = tk.Button(frame, text="9", command=lambda: on_click_button_number(9))
button_0 = tk.Button(frame, text="0", command=lambda: on_click_button_number(0))

button_1.grid(column=2, row=2)
button_2.grid(column=3, row=2)
button_3.grid(column=4, row=2)
button_4.grid(column=2, row=3)
button_5.grid(column=3, row=3)
button_6.grid(column=4, row=3)
button_7.grid(column=2, row=4)
button_8.grid(column=3, row=4)
button_9.grid(column=4, row=4)
button_0.grid(column=3, row=5)

mc.grid(column=6, row=5)
mplus.grid(column=5, row=3)
mminus.grid(column=6, row=3)
ms.grid(column=5, row=4)
mr.grid(column=6, row=4)
ce.grid(column=5, row=2)
ac.grid(column=6, row=2)

dot.grid(column=4, row=5)
sqrt.grid(column=2, row=5)

button_plus.grid(column=1, row=2)
button_minus.grid(column=1, row=3)
button_multiplication.grid(column=1, row=4)
button_division.grid(column=1, row=5)

change_sign.grid()

enter.grid()

label = tk.Label(frame, textvariable=memory)
label.grid()

frame.grid()

window.mainloop()
