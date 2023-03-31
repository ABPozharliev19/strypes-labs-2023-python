from typing import List, Tuple, Union, Optional

from db import Db, FILMS
from entities.entity import Entity, EntityType


class FilmsManager:
    def __init__(self):
        self.db = Db()

    def get(self) -> List[Entity]:
        """
        Returns all entities

        Returns:
            List[Entity]
        """
        return self.db.get_entities_by_type(FILMS)

    def get_by_id(self, identifier: int) -> Optional[Entity]:
        """
        Returns entities which have a certain id

        Args:
            identifier:

        Returns:
            List[Entity]
        """
        return self.db.get_entity_by_id(FILMS, identifier)

    def update_by_id(self, identifier: int, new_values: EntityType) -> bool:
        entity = self.db.get_entity_by_id(FILMS, identifier)

        try:
            entity.name = new_values.get("name")
            entity.year = new_values.get("year")
            entity.genre = new_values.get("genre")
        except ValueError:
            return False

        self.db.update_entity_by_id(FILMS, identifier, entity)

        return True

    def delete_by_id(self, identifier: int) -> bool:
        """
        Deletes an entity which has a certain id

        Args:
            identifier:

        Returns:
            bool: True if entity was deleted successfully, False otherwise
        """
        return self.db.delete_entity_by_id(FILMS, identifier)

    def create_entity(self, new_values: EntityType):
        return self.db.create_entity(FILMS, new_values)

    def search(self, name: str = None, year: str = None, genre: str = None) -> List[EntityType]:
        return self.db.search(name=name, year=year, genre=genre)