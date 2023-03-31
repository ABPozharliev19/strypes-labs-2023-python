from tkinter import *
from core.films import FilmsManager


class GamesView:
    def __init__(self):
        self.games_manager = FilmsManager()
        self.root = Tk()

        self.current_entities = []

        self.name_label = Label(self.root, text="Name", font=("Arial", 14))
        self.year_label = Label(self.root, text="Year", font=("Arial", 14))
        self.genre_label = Label(self.root, text="Genre", font=("Arial", 14))

        self.name_entry = Entry(self.root, font=("Arial", 14))
        self.year_entry = Entry(self.root, font=("Arial", 14))
        self.genre_entry = Entry(self.root, font=("Arial", 14))

        self.name_label.grid(row=0, column=0)
        self.year_label.grid(row=1, column=0)
        self.genre_label.grid(row=2, column=0)

        self.name_entry.grid(row=0, column=1)
        self.year_entry.grid(row=1, column=1)
        self.genre_entry.grid(row=2, column=1)

        self.submit_button = Button(self.root, text="Submit", command=self.create_entity, font=("Arial", 14))
        self.submit_button.grid(row=3, column=0)

        self.update_button = Button(self.root, text="Update", command=self.update_entity, font=("Arial", 14))
        self.update_button.grid(row=3, column=1)

        self.delete_button = Button(self.root, text="Delete", command=self.delete_entity, font=("Arial", 14))
        self.delete_button.grid(row=3, column=2)

        self.listbox = Listbox(self.root, font=("Arial", 14))
        self.listbox.grid(row=4, column=0, columnspan=3)

        self.listbox.bind('<<ListboxSelect>>', self.select_entity)

        self.refresh_listbox()

        self.search_name_label = Label(self.root, text="Search by Name", font=("Arial", 14))
        self.search_year_label = Label(self.root, text="Search by Year", font=("Arial", 14))
        self.search_genre_label = Label(self.root, text="Search by Genre", font=("Arial", 14))

        self.search_name_entry = Entry(self.root, font=("Arial", 14))
        self.search_year_entry = Entry(self.root, font=("Arial", 14))
        self.search_genre_entry = Entry(self.root, font=("Arial", 14))

        self.search_name_label.grid(row=5, column=0)
        self.search_year_label.grid(row=6, column=0)
        self.search_genre_label.grid(row=7, column=0)

        self.search_name_entry.grid(row=5, column=1)
        self.search_year_entry.grid(row=6, column=1)
        self.search_genre_entry.grid(row=7, column=1)

        self.search_button = Button(self.root, text="Search", command=self.search_entities, font=("Arial", 14))
        self.search_button.grid(row=8, column=0, columnspan=3)

    def search_entities(self) -> None:
        name = self.search_name_entry.get()
        year = self.search_year_entry.get()
        genre = self.search_genre_entry.get()

        search_criteria = {}
        if name:
            search_criteria["name"] = name
        if year:
            search_criteria["year"] = year
        if genre:
            search_criteria["genre"] = genre

        entities = self.games_manager.search(name=search_criteria.get("name"), year=search_criteria.get("year"), genre=search_criteria.get("genre"))
        self.listbox.delete(0, END)

        for entity in entities:
            self.listbox.insert(END, entity.name)

        self.current_entities = entities

    def refresh_listbox(self) -> None:
        self.listbox.delete(0, END)
        entities = self.games_manager.get()
        self.current_entities = entities
        for entity in entities:
            self.listbox.insert(END, entity.name)

    def create_entity(self) -> None:
        name = self.name_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()
        new_entity = {"name": name, "year": year, "genre": genre}
        self.games_manager.create_entity(new_entity)
        self.refresh_listbox()

    def update_entity(self) -> None:
        selected_entity = self.listbox.curselection()
        if selected_entity:
            identifier = selected_entity[0]
            name = self.name_entry.get()
            year = self.year_entry.get()
            genre = self.genre_entry.get()
            new_entity = {"name": name, "year": year, "genre": genre}
            self.games_manager.update_by_id(identifier, new_entity)
            self.refresh_listbox()

    def delete_entity(self) -> None:
        selected_entity = self.listbox.curselection()
        if selected_entity:
            identifier = selected_entity[0]
            self.games_manager.delete_by_id(identifier)
            self.refresh_listbox()

    def select_entity(self, event) -> None:
        selected_entity = self.listbox.curselection()
        if selected_entity:
            identifier = self.current_entities[selected_entity[0]].id
            print(identifier)
            entity = self.games_manager.get_by_id(identifier)
            self.name_entry.delete(0, END)
            self.name_entry.insert(END, entity.name)
            self.year_entry.delete(0, END)
            self.year_entry.insert(END, entity.year)
            self.genre_entry.delete(0, END)
            self.genre_entry.insert(END, entity.genre)

    def run(self) -> None:
        self.root.mainloop()