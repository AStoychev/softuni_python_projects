from abc import ABC, abstractmethod

from project.core.validator import Validator


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_value_error_if_string_is_empty_ot_white_space(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_value_error_if_value_is_equal_or_less_than_zero(value, "Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"