from abc import ABC, abstractmethod

from project.core.validaror import Validator


class Car(ABC):
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.raise_if_word_is_less_than(value, 4, f"Model {value} is less than 4 symbols!")
        self.__model = value
    
    @property
    def speed_limit(self):
        return self.__speed_limit
    
    @speed_limit.setter
    def speed_limit(self, value):
        Validator.raise_is_number_not_in_range(value,
                                               self.min_speed_limit,
                                               self.max_speed_limit,
                                               f"Invalid speed limit! Must be between {self.min_speed_limit}"
                                               f" and {self.max_speed_limit}!")
        self.__speed_limit = value
    
    @property
    @abstractmethod
    def min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def max_speed_limit(self):
        pass