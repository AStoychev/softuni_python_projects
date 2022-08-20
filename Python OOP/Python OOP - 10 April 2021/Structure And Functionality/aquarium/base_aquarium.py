from abc import ABC, abstractmethod

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def calculate_comfort(self):
        return sum(c.comfort for c in self.decorations)

    def add_fish(self, fish: BaseFish):
        if self.capacity <= len(self.fish):
            return "Not enough capacity."

        if self.fish_type != fish.__class__.__name__:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_status = "none" if len(self.fish) == 0 else " ".join([f.name for f in self.fish])
        return f"{self.name}:\nFish: {fish_status}\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"