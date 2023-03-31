from typing import TypedDict, Dict, Literal, Union

EntityType = TypedDict("EntityType", {
    "name": str,
    "year": str,
    "genre": str
})


class Entity:
    def __init__(self, entity_type: Literal["films", "games", "books"], identifier: str, game: EntityType):
        self.type = entity_type
        self.id = int(identifier)
        self._name = game.get("name")
        self._year = int(game.get("year"))
        self._genre = game.get("genre")

    def __repr__(self) -> str:
        """
        Returns human-readable presentation for the object

        Returns:
            str
        """
        return f"Entity('type': {self.type}, 'id': {self.id}, 'name': {self._name}, 'year': {self._year}, 'genre': {self._genre})"

    def to_dict(self) -> Dict:
        """
        Converts the class properties to a dict

        Returns:
            Dict
        """
        return {
            "name": self._name,
            "year": self._year,
            "genre": self._genre
        }

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, new_year: Union[str, int]) -> None:
        if isinstance(new_year, str):
            try:
                new_year = int(new_year)

                self._year = new_year
            except:
                raise ValueError("Age is not an integer")
        elif isinstance(new_year, int):
            self._year = new_year
        else:
            raise ValueError("Age is not an integer")

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, new_genre: str) -> None:
        self._genre = new_genre
