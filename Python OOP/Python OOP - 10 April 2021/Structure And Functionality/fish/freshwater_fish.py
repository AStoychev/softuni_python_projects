from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    EAT = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += self.EAT