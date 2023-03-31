import tkinter as tk


def calculate_bmi():
    global bmi_label
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = round(weight / (height * height), 2)
    bmi_label.config(text=f"Your BMI is {bmi}")


window = tk.Tk()
window.title("BMI Calculator")

height_label = tk.Label(window, text="Enter your height in meters:")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Enter your weight in kilograms:")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

bmi_label = tk.Label(window, text="")
bmi_label.pack()

window.mainloop()