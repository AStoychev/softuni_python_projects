from project.car.car import Car
from project.core.validaror import Validator


class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_contains_empty_string_or_white_space(value,
                                                                       f"Name should contain at least one character!")
        self.__name = value

    def change_car(self, car: Car):
        car.is_taken = True
        if self.car is None:
            self.car = car
            return f"Driver {self.name} chose the car {car.model}."

        self.car.is_taken = False
        old_model = self.car.model
        self.car = car
        return f"Driver {self.name} changed his car from {old_model} to {car.model}."