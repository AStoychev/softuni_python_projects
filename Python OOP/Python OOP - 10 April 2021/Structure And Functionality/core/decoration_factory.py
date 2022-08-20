from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationFactory:

    decoration_types = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    def create_decoration(self, decoration_type):
        if decoration_type not in self.decoration_types:
            raise ValueError("Invalid decoration type.")
        return self.decoration_types[decoration_type]()