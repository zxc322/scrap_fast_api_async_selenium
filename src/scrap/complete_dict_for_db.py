from bs4_parse import BS4Parse



class CompleteDict:

    def __init__(self, cls: BS4Parse) -> None:
        self.parse = cls


    def user_insert(self):
        user = dict(
            name = self.parse.creator_name(),
            profile_url = self.parse.profile_url(),
            phone = self.parse.phone(),
            type = self.parse.creator_type(),
            listings = self.parse.listing(),
            website_url = self.parse.website_url(),
            on_kijiji_from = self.parse.on_kijiji_from(),
            avg_reply = self.parse.avg_reply(),
            reply_rate = self.parse.reply_rate()
        )

        return user
    
    def item_insert(self):
        item = dict(
            ad_id = self.parse.ad_id(),
            location = self.parse.location(),
            address = self.parse.address(),
            published_date = self.parse.published_date(),
            description = self.parse.description()
        )

        return item

    def overview_dict(self):
        hhw = self.parse.hydro_heat_water()
        overview = dict(
            hydro = 'Yes: Hydro' in hhw,
            heat = 'Yes: Heat' in hhw,
            water = 'Yes: Water' in hhw,
            wifi = self.parse.wifi(),
            parking = self.parse.parking(),
            agreement_type = self.parse.agreement_type(),
            move_in_date = self.parse.move_in_date(),
            pet_friendly = self.parse.pet_friendly()
        )

        return overview


    
    def unit_dict(self):
        apps = self.parse.appliances()
        if apps:
            apps_dict = dict(
                laundry_in_unit = apps[0],
                lundry_in_building = apps[1],
                dishwasher = apps[2],
                fridge = apps[3]
            )
        units = dict(
            size = self.parse.size(),
            furnished = self.parse.furnished(),
            air_conditioning = self.parse.air_condition(),
            outdoor_spase = self.parse.outdoor(),
            smoking_permitted = self.parse.smoking()
        )

        if apps_dict:
            units.update(apps_dict)
        return units
