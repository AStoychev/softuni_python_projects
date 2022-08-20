from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class TableFactory:
    tables_types = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def create_table(self, table_type, table_number, capacity):
        return self.__class__.tables_types[table_type](table_number, capacity)