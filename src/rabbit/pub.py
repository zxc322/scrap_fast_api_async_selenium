#!/usr/bin/env python
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from rabbit.pika_connect import connection

channel = connection.channel()
channel2 = connection.channel()


channel.queue_declare(queue='Q1')
channel2.queue_declare(queue='Q2')

data = [{"name": "Madison Ridge", "profile_url": "/o-madison-ridge/1017080421/listings/1?referral=organic", "phone": "1-844-550-2074", "type": "Professional", "listings": 1, "website_url": "https://centurion.leadmanaging.com/application/controllers/booking.php?r=nkj2QUExMDExNjM%3D&utm_campaign=kijiji_vdp&utm_medium=referral&utm_source=kijiji", "on_kijiji_from": "May 2013", "avg_reply": None, "reply_rate": None}, {"ad_id": 1627087618, "location": "Regina, Saskatchewan", "address": "1251 \u2022 1261 \u2022 1271 \u2022 1281 McEachern Drive, Regina, SK, S4X 0N3", "published_date": "2022-11-18T00:32:08.000Z", "description": "DescriptionLocated on McEachern Drive, this beautiful low-rise property offers twoand three-bedroom apartments. Madison Ridge is a four-building complex in the Hawkstone neighbourhood of Northwest Regina. Residents will enjoy a family-friendly modern lifestyle close to parks, playgrounds, restaurants, stores, services, and future schools.PROMOTION: Receive $500 OFF first month's rent when you move in by December 1st, 2022! *Some conditions apply, please inquire for more details.***6- or 12-month lease options available!**TOUR OPTIONS:In-personVirtualSuite offers:Central heating and air conditioningFull-sized stainless steel appliances, including microwaveIn-suite laundryIn-suite storagePrivate balconies in each unit for an extended living spaceProperty offers:Pet-friendlyEV parkingYour community offers:Easy access to Louis Riel Trailand CanAm HighwayShort drive to shopping centreShort distance to schools and parksFees:*Security Deposit - $499*Hydro not included*Pets Fee: $200 non-refundable fee + $25/pet/month. Maximum of 2 pets allowed.Outdoor Parking: $50/month for additional spot. *Rent includes one electrified parking stall.Storage: $40/monthCall our Customer Care Centre today! We're open Monday - Friday 9am-9pmET. Saturday - Sunday 10am-6:30pmET.How to get in touch with us:Text #book to: 1-844-550-2007Call our Customer Care Centre: 1-844-550-2074Copy/paste this link into your browser to book an appointment today: http://bit.ly/MadisonRidgeBook\"Suite images shown represent standard unit finishes, which may differ between units. Suite layout varies.\"Show more"}, {"hydro": False, "heat": False, "water": False, "wifi": False, "parking": 1, "agreement_type": "1 Year", "move_in_date": None, "pet_friendly": "Yes"}, {"size": None, "furnished": False, "air_conditioning": False, "outdoor_spase": "Balcony", "smoking_permitted": False, "laundry_in_unit": True, "lundry_in_building": False, "dishwasher": False, "fridge": True}]

print(type(data))
import json
j = json.dumps(data)
print('dumps to', type(j))

while True:

    ch = int(input('chose 1 or 2: '))
    msg = input('message: ')
    if ch == 1:
        channel.basic_publish(exchange='', routing_key='Q1', body=msg)
        print(f" [x] Sent {msg} to ch1")
    elif ch == 2:
        channel2.basic_publish(exchange='', routing_key='Q2', body=j)
        print(f" [x] Sent {msg} to ch2")

