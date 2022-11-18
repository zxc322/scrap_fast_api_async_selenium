import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import json
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constant import *
from selenium.webdriver.common.by import By
import time 
from bs4_parse import BS4Parse
from complete_dict_for_db import CompleteDict
from rabbit.links_consumer import RabbitLinksConsumer
from rabbit.items_data_publisher import RabbitDataPublisher

class ItemScraper():

    # def __init__(self):
    #     self.rabbit_consumer = RabbitLinksConsumer()
        


    def item_scraper(self, url):
        try:
            print(f'--- parsing item => {url} ---')
            driver = Remote(
                command_executor='http://chrome:4444/wd/hub',
                options=options,
                desired_capabilities=DesiredCapabilities.CHROME
                )

            driver.get(url)      
            try:
                print('--- WE are looking for reveal btn ---   ')
                time.sleep(3)
                reveal_button = driver.find_element(By.XPATH, "//button[@class='phoneNumberContainer-69344174 phoneShowNumberButton-1052915314 button-1997310527 button__medium-1066667140']")
                print(f'---reveal btn {reveal_button} ---')
                reveal_button.click()
                print('--- click ---')
                time.sleep(3)
            except Exception as ex:
                print(f'--- no phone button coz {ex} ---')
            html = driver.page_source

            to_parse = BS4Parse(html=html)
            complete_dict = CompleteDict(to_parse)    

            user_dict = complete_dict.user_insert()
            item_dict = complete_dict.item_insert()
            overview_dict = complete_dict.overview_dict()
            units_dict = complete_dict.unit_dict()

            data = [user_dict, item_dict, overview_dict, units_dict]
            to_rabbit = json.dumps(data)
            print(type(to_rabbit    ))
            print('!---ITEM\n', to_rabbit)

            RabbitDataPublisher.send_message(body=to_rabbit)
            # new_item_id = self.db.get_or_create_item(item_data=item_dict, user_data=user_dict)
            # if not new_item_id.created_before:
            #     self.db.create_overview(item_id=new_item_id, overview_dict=overview_dict)
            #     self.db.create_units(item_id=new_item_id, units_dict=units_dict)
            
            # self.chanel2.basic_publish(exchange='',
            #         routing_key='items_data',
            #         body='send_new_item')

            
            
        except Exception as ex:
            print(f'--- exc in item_scraper {ex} ---')
        finally:
            driver.quit()
            driver.close()