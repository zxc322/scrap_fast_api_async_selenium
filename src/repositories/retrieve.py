import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from repositories.generic import GenericInit
from sqlalchemy import select
from schemas import retrieve as schema_r
from typing import Optional


class Retrieve(GenericInit):

    def get_items(self, conditions):
        conditions = conditions.dict(skip_defaults=True)

        
    def get_user_by_profile_link(self, link: str) -> Optional[int]:
        user = self.db.fetch_one(select(self.users.c.user_id).select_from(
            self.users).where(
                self.users.c.profile_url==link)
        )
        return user

    def get_item_by_ad_ID(self, ad_id: int) -> Optional[int]:
        item = self.db.fetch_one(select(self.items.c.item_id).select_from(
            self.items).where(
                self.items.c.ad_id==ad_id)
        )
        return item

