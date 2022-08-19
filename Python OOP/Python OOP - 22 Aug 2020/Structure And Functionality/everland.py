from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses + room.room_cost
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.budget >= total_cost:
                room.budget -= total_cost
                result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return "\n".join(result)

    def status(self):
        result = ""
        result += f"Total population: {sum([x.members_count for x in self.rooms])}\n"
        for x in self.rooms:
            result += f"{x.family_name} with {x.members_count} members. Budget: {x.budget:.2f}$, Expenses: {x.expenses:.2f}$\n"
            if x.children:
                counter = 0
                for c in x.children:
                    counter += 1
                    result += f"--- Child {counter} monthly cost: {(c.cost * 30):.2f}$\n"
            if hasattr(x, "appliances"):
                total_expenses = 0
                for a in x.appliances:
                    total_expenses += a.get_monthly_expense()
                result += f"Appliances monthly cost: {total_expenses:.2f}$\n"

        return result