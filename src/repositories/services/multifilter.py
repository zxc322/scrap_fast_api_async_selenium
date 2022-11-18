class MultiFilter:


    def retrieve_item(self, conditions):
        query = "SELECT\
            ad_id,\
            location,\
            address,\
            published_date,\
            price,\
            name as creator_name,\
            type as creator_type,\
            listings as creators_total_listings,\
            time_on_kijiji,\
            avg_reply,\
            reply_rate,\
            hydro, heat, water, wifi, parking,\
            agreement_years,\
            pet_friendly,\
            size, furnished, laundry, dishwasher, fridge,\
            air_Conditioning, outdoor_spase, smoking_permitted\
            FROM items\
            JOIN users\
            ON items.creator.id = users.user_id\
            JOIN overview\
            ON items.item_id = overwiev.item_id\
            JOIN unit\
            ON items.item_id = unit.item_id"

        query += self.__generate_filters(conditions)
        query += " ORDER BY "
        return query

    def __generate_filters(self, conditions):
        filters = " WHERE items.item_id IS NOT NULL"
        for k, v in conditions.items():
            if isinstance(v, list):
                filters += f" AND {k} BETWEEN {str(v[0])} AND {str(v[1])}"
            else:
                filters += f" AND {k} = {str(v)}" 
        return filters



query = MultiFilter()
conditions = {"price": [500, 1000]}
print(query.retrieve_item(conditions))