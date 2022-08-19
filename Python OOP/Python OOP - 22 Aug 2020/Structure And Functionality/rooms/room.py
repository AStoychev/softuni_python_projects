from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for el in args:
            for current_el in el:
                if isinstance(current_el, Appliance):
                    total_expenses += current_el.get_monthly_expense()
                elif isinstance(current_el, Child):
                    total_expenses += current_el.cost * 30
        self.expenses += total_expenses