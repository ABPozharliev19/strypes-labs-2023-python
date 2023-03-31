from typing import Literal, Dict, List, Union, Optional
import json

from entities.entity import Entity, EntityType

FILMS: Literal["films"] = "films"
GAMES: Literal["games"] = "games"
BOOKS: Literal["books"] = "books"

LiteralType = Literal["films", "games", "books"]


class Db:
    def __init__(self):
        self.file = open("db.json", "r+")
        self.entities: Dict[str, Dict] = json.load(self.file)

    def _write_to_file(self):
        self.file.seek(0)
        self.file.truncate(0)
        json.dump(self.entities, self.file, indent=4)

    def _construct_entity(self, entity_type: LiteralType, entity: Dict) -> Entity:
        """
        Constructs an entity based on the entity type

        Args:
            entity_type: Literal["films", "games", "books"]
            entity: Dict

        Returns:
            Entity
        """
        identifier = next(iter(entity.keys()))
        values = next(iter(entity.values()))

        return Entity(entity_type=entity_type, identifier=identifier, game=values)

    def _get_last_id(self, entity_type: str) -> int:
        """

        Args:
            entity_type:

        Returns:

        """
        if entity_type not in self.entities:
            return 0

        highest_id = 0

        for entity_id in self.entities[entity_type]:
            if int(entity_id) > highest_id:
                highest_id = int(entity_id)

        return highest_id

    def get_entities_by_type(self, entity_type: LiteralType) -> List[Entity]:
        """
        Returns all entities that are a certain type

        Args:
            entity_type: Literal["films", "games", "books"]

        Returns:

        """
        raw_entities = self.entities.get(entity_type)
        entities = []

        for key, value in raw_entities.items():
            entities.append(self._construct_entity(entity_type=entity_type, entity={key: value}))

        return entities

    def get_entity_by_id(self, entity_type: LiteralType, identifier: int) -> Optional[Entity]:
        """
        Returns an entity with a certain id

        Args:
            entity_type: LiteralType
            identifier: int

        Returns:
            Optional[Entity]
        """
        entities = self.get_entities_by_type(entity_type)

        try:
            return next(iter((filter(lambda x: x.id == identifier, entities))))
        except StopIteration:
            return None

    def update_entity_by_id(self, entity_type: LiteralType, identifier: int, new_entity: Entity) -> None:
        """
        Updates an entity with new values

        Args:
            entity_type: LiteralType
            identifier: int
            new_entity: Entity

        Returns:
            None
        """
        self.entities[entity_type][str(identifier)]["name"] = new_entity.name
        self.entities[entity_type][str(identifier)]["year"] = new_entity.year
        self.entities[entity_type][str(identifier)]["genre"] = new_entity.genre

        self._write_to_file()

    def create_entity(self, entity_type: LiteralType, entity: EntityType) -> None:
        """
        Creates a new entity of the specified type and adds it to the database

        Args:
            entity_type: LiteralType
            entity: Entity

        Returns:
            None
        """
        entity_dict = {"name": entity.get("name"), "year": entity.get("year"), "genre": entity.get("genre")}
        entity_id = self._get_last_id(entity_type) + 1

        if entity_id in self.entities[entity_type]:
            raise ValueError("Entity with this ID already exists.")

        self.entities[entity_type][entity_id] = entity_dict
        self._write_to_file()

    def delete_entity_by_id(self, entity_type: LiteralType, identifier: int) -> None:
        """
        Deletes the entity with the specified ID from the database

        Args:
            entity_type: LiteralType
            identifier: int

        Returns:
            None
        """
        entity_id = str(identifier)

        if entity_id not in self.entities[entity_type]:
            raise ValueError("Entity with this ID does not exist.")

        del self.entities[entity_type][entity_id]
        self._write_to_file()

    def search(self, name: str = None, year: str = None, genre: str = None) -> List[EntityType]:
        results = []
        for entity_type in self.entities:
            for entity_id, entity in self.entities[entity_type].items():
                if (not name or entity["name"].lower() == name.lower()) and \
                        (not year or int(entity["year"]) == int(year)) and \
                        (not genre or entity["genre"].lower() == genre.lower()):
                    entity["id"] = int(entity_id)
                    entity["type"] = entity_type
                    results.append(entity)

        for index, i in enumerate(results):
            results[index] = Entity(i.get("type"), i.get("id"), i)

        print(results)

        return results
