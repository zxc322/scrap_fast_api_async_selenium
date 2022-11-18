import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from typing import Dict, Optional
from datetime import datetime

from repositories.generic import GenericInit
from repositories.retrieve import Retrieve
from schemas import retrieve as schema_r
from schemas import create as schema_c


class Insert(GenericInit):

    def get_or_create_user(self, user_data: Dict) -> schema_r.ResponseId:
        user = Retrieve(db=self.db).get_user_by_profile_link(user_data.get('profile_url'))
        print('line3 GoC user. User = ', user)
        # if user:
        #     return schema_r.ResponseId(id=user)
        user_data.update(created_at=datetime.utcnow())
        user_id = self.db.execute(self.users.insert().values(user_data))
        #return schema_r.ResponseId(id=user_id)
        return user_id

    
    def get_or_create_item(self, item_data: Dict, user_data: Dict) -> Optional[schema_r.ResponseId]:
        item = Retrieve().get_item_by_ad_ID(item_data.get('ad_id'))
        if item:
            return schema_c.ItemCreated(id=item, created_before=True)
        user_id = self.get_or_create_user(user_data=user_data)
        item_data.update(created_at=datetime.utcnow(), user_id=user_id.id)
        item_id = self.db.execute(self.items.insert().values(item_data))
        return schema_c.ItemCreated(id=item_id, created_before=False)

    def create_overview(self, item_id: int, overview_dict: Dict) -> schema_r.ResponseId:
        overview_dict.update(item_id=item_id)
        return schema_r.ResponseId(id= self.db.execute(self.overview.insert().values(overview_dict)))


    def create_units(self, item_id: int, units_dict: Dict) -> schema_r.ResponseId:
        units_dict.update(item_id=item_id)
        return schema_r.ResponseId(id=self.db.execute(self.units.insert().values(units_dict)))