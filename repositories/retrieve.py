from repositories.generic import GenericInit



class Retrieve(GenericInit):

    async def get_items(self, conditions):
        conditions = conditions.dict(skip_defaults=True) 