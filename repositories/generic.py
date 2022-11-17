from db.models import users_table, items_table, overviews_table, units_table


class GenericInit:

    def __init__(self):
        self.users = users_table
        self.items = items_table
        self.overview = overviews_table
        self.units = units_table