from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    EAT = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += self.EAT