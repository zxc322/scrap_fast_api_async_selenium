from bs4 import BeautifulSoup as BS
import re
from typing import Optional
from datetime import datetime

class BS4Parse:

    def __init__(self, html) -> None:
        self.soup = BS(html, 'lxml')


    def creator_name(self):
        try:
            name = self.soup.find('div', class_='header-683592183').get_text(strip=True)
            return name
        except:
            return None

    
    def profile_url(self):
        try:
            profile_url = self.soup.find('a', class_="link-2686609741").get('href')
            return profile_url
        except:
            return None


    def phone(self):
        try:
            phone = self.soup.find('span', class_='phoneShowNumberButton-1052915314').find('span').get_text(strip=True)
            return phone
        except:
            return None

    def creator_type(self):
        try:
            type = self.soup.find('div', class_='line-2791721720').get_text(strip=True)
            return type
        except:
            return None


    def on_kijiji_from(self):
        try:
            date = self.soup.find('div', {"data-qa-id": re.compile("member-since-stat")}).find(
                "span", class_="date-862429888"). get_text(strip=True)
            return date
        except:
            return None


    def listing(self):
        try:
            listing = self.soup.find('use', {"xlink:href": "#icon-listing"}).parent.parent.find("span").get_text()
            listing = int(listing)
            return listing
        except:
            return None


    def website_url(self):
        try:
            creator_block = self.soup.find_all("div", class_="line-2791721720")
            for item in creator_block:
                url = item.find('a', {"rel": "noopener noreferrer"})
                if url:
                    website_url = url.get('href')
                    return website_url
        except:
            return None

    
    def avg_reply(self):
        try:
            avg_reply = self.soup.find('div', {"data-qa-id": "responsiveness-stat-block"}).find(
                'div', class_='text-910784403').get_text(strip=True)
            return int(avg_reply) if avg_reply.isnumeric() else avg_reply
        except:
            return None

    def reply_rate(self):
        try:
            reply_rate = self.soup.find('div', {"data-qa-id": "reply-rate-stat-block"}).find(
                'div', class_='text-910784403').get_text(strip=True)
        except:
            return None
    
    

    def ad_id(self):
        try:
            ad_id = self.soup.find('li', class_='currentCrumb-3831268168').get_text(strip=True)
            return ad_id[5:]
        except:
            return None


    def location(self):
        try:
            location = self.soup.find('button', {"id": "SearchLocationPicker"}).get_text(strip=True)
            return location
        except:
            return None


    def title(self):
        try:
            title = self.soup.find_all('span', {"itemprop": "name"})[-1].get_text(strip=True)
            return title
        except Exception:
            title = self.soup.find_all('h1', class_='title-2323565163')[-1].get_text(strip=True)
            return title
        except:
            return None

    def address(self):
        try:
            address = self.soup.find(
                'div', class_='locationRow-2870378686').find(
                    'div', class_='locationContainer-2867112055').find(
                        'span', {"itemprop": "address"}).get_text(strip=True)
            return address
        except:
            return None

    
    def published_date(self):
        try:
            time = self.soup.find('time').get('datetime')
            return time
        except:
            return None


    def price(self):
        try:
            price = self.soup.find('div', class_='priceWrapper-1165431705').find('span').get('content')[:-1]
            print('bs4 price', price)
            price = int(price)
            return price
        except:
            return None


    def description(self):
        try:
            description = self.soup.find('div', class_="root-2377010271 light-3420168793 card-745541139").get_text(strip=True)
            description.replace(r'\n', '')
            return description
        except:
            return None


    def hydro_heat_water(self):
        try:
            # return example [None, 'Yes: Hydro', 'Yes: Heat', 'Yes: Water']
            container = self.soup.find('svg', class_="icon-459822882 attributeGroupIcon-3454750106").parent.find_all('svg')
            utilits = [x.get('aria-label') for x in container]
            return utilits
        except:
            return []


    def wifi(self):
        try:
            wifi = self.soup.find('use', {"xlink:href": "#icon-attribute-group-wifiandmore"}).parent.parent.get_text()
            wifi = 'Included' in wifi and 'Not Included' not in wifi
            return wifi
        except:
            return False

       
    def parking(self):
        try:
            parking = self.soup.find('use', {"xlink:href": "#icon-attributes-numberparkingspots"}).parent.parent.get_text().replace('Parking Included', '')
            parking = int(parking)
            return parking
        except:
            return 0
  
    def agreement_type(self):
        try:
            agr_type = self.soup.find('use', {"xlink:href": "#icon-attributes-agreementtype"}).parent.parent.get_text().replace('Agreement Type', '')
            return agr_type
        except:
            return None

            
    def move_in_date(self):
        try:
            date = self.soup.find('use', {"xlink:href": "#icon-attributes-dateavailable"}).parent.parent.get_text().replace('Move-In Date', '')
            return date
        except:
            return None


    def pet_friendly(self):
        try:
            pet = self.soup.find('use', {"xlink:href": "#icon-attributes-petsallowed"}).parent.parent.get_text().replace('Pet Friendly', '')
            return pet
        except:
            return None


    def size(self):
        try:
            size = self.soup.find('use', {"xlink:href": "#icon-attributes-areainfeet"}).parent.parent
            size = int(size.find('dd', class_='twoLinesValue-2815147826').get_text().replace(',', ''))
            return size
        except:
            return None
    

    def furnished(self):
        try:
            furnished = self.soup.find('use', {"xlink:href": "#icon-attributes-furnished"}).parent.parent.find(
                'dd', 'twoLinesValue-2815147826').get_text()
            furnished = 'Yes' in furnished
            return furnished
        except:
            return False


    def appliances(self):
        try: 
            # return example [True, False, False, True] or []
            appliances_block = self.soup.find('use', {"xlink:href": "#icon-attribute-group-appliances"}).parent.parent
            all_appliances = appliances_block.find('ul', 'list-1757374920 disablePadding-1318173106').get_text(strip=True)
            result = list()
            result.append('Laundry (In Unit)' in all_appliances)
            result.append('Laundry (In Building)' in all_appliances)
            result.append('Dishwasher' in all_appliances)
            result.append('Fridge / Freezer' in all_appliances)
            return result
        except:
            return []


    def air_condition(self) -> bool:
        try:
            air_condition = self.soup.find('use', {"xlink:href": "#icon-attributes-airconditioning"}).parent.parent.find(
                'dd', class_='twoLinesValue-2815147826').get_text()
            air_condition = 'Yes' in air_condition
            return air_condition
        except:
            return False


    def outdoor(self) -> Optional[str]:
        try:
            outdoor = self.soup.find('use', {"xlink:href": "#icon-attribute-group-outdoorspace"}).parent.parent.find(
                'ul', 'list-1757374920 disablePadding-1318173106').get_text(strip=True)
            return outdoor
        except:
            return None

    
    def smoking(self) -> bool:
        try:
            smoke = self.soup.find('use', {"xlink:href": "#icon-attributes-smokingpermitted"}).parent.parent.find(
                'dd', class_='twoLinesValue-2815147826').get_text()
            smoke = 'Yes' in smoke
            return smoke
        except:
            return False