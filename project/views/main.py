import tkinter
from tkinter import ttk

from .base import BaseView


class MainMenu(BaseView):
    def __init__(self, window: tkinter.Tk):
        self.frame = tkinter.Frame(window)

        self.frame.grid(row=0, column=0, sticky="")

        self.film_button = ttk.Button(master=self.frame, text="Films")
        self.games_button = ttk.Button(master=self.frame, text="Games")
        self.books_button = ttk.Button(master=self.frame, text="Books")

    def render(self):
        self.configure()

        self.frame.pack()

    def configure(self):
        self.film_button.pack()
        self.games_button.pack()
        self.books_button.pack()
