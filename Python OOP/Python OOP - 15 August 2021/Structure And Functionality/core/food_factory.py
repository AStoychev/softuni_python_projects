from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class FoodFactory:

    food_types = {
        "Bread": Bread,
        "Cake": Cake
    }

    def create_food(self, food_type, name, price):
        return self.__class__.food_types[food_type](name, price)