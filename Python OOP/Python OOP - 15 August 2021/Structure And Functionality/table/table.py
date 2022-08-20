from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.core.validator import Validator
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.raise_if_number_not_in_range(value, self.min_number, self.max_number, self.table_number_error_message)
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_value_error_if_value_is_equal_or_less_than_zero(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def min_number(self):
        return

    @property
    @abstractmethod
    def max_number(self):
        return

    @property
    @abstractmethod
    def table_number_error_message(self):
        return

    def reserve(self, number_of_people):
        if self.capacity >= number_of_people:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)
        return bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"