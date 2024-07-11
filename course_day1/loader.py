import csv
from typing import List


class Pokemon:
    def __init__(self, keymap: dict) -> None:
        self.number = int(keymap["#"])
        self.name = keymap["Name"]
        self.type_1 = keymap["Type 1"]
        self.type_2 = keymap["Type 2"]
        self.total = keymap["Total"]
        self.hp = keymap["HP"]
        self.attack = keymap["Attack"]
        self.defense = keymap["Defense"]
        self.sp_atk = keymap["Sp. Atk"]
        self.sp_def = keymap["Sp. Def"]
        self.speed = keymap["Speed"]
        self.generation = keymap["Generation"]
        self.legendary = keymap["Legendary"]
        pass


def read(path: str) -> List[Pokemon]:
    with open(path) as file:
        result = csv.DictReader(file)
        return [Pokemon(monster) for monster in result]


class LazyLoader:
    def __init__(self, path: str) -> None:
        self.path = path
        self.cache = None

    def get(self) -> List[Pokemon]:
        if self.cache is None:
            self.cache = read(self.path)
        return self.cache
