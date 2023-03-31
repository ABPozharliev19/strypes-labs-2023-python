import tkinter.ttk as ttk
from tkinter import Tk
import tkinter

from views.base import BaseView
from views.main import MainMenu


class ViewManager:
    def __init__(self, window: Tk):
        self.window = window
        self.window.geometry("600x400")
        self.window.resizable(width=False, height=False)
        self.window.title("Collection Manager")

        self.main_menu = MainMenu(window)

        self.main_menu.render()
        self.window.mainloop()
