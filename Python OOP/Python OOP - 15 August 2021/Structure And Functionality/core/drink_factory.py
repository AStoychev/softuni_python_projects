from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    drink_types = {
        "Tea": Tea,
        "Water": Water
    }

    def create_drink(self, drink_type, name, portion, brand):
        return self.__class__.drink_types[drink_type](name, portion, brand)