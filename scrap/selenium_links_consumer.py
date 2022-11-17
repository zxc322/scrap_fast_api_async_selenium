from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constant import *
from selenium.webdriver.common.by import By

from bs4_parse import BS4Parse


class LinkConsumer():

    def __init__(self):
        self.chanel = connection.channel()
        self.chanel.queue_declare('items_urls')

    

    def item_scraper(self, url):
        try:
            print('--- parsing item... ---')
            driver = Remote(
                command_executor='http://chrome:4444/wd/hub',
                options=options,
                desired_capabilities=DesiredCapabilities.CHROME
                )

            driver.get(url)      
            try:
                reveal_button = driver.find_element(By.XPATH, "//button[@class='phoneNumberContainer-69344174 phoneShowNumberButton-1052915314 button-1997310527 button__medium-1066667140']")
                
                reveal_button.click()
                print('--- click ---')
                time.sleep(3)
            except Exception as ex:
                print(f'--- no phone button coz {ex} ---')
            html = driver.page_source
            import time
            now = time.time()
            with open('data/'+str(now)+'.html', 'w') as f:
                f.write(html)

            to_parse = BS4Parse(html=html)

            to_parse.creator_name()
            to_parse.profile_url()
            to_parse.phone()        
            to_parse.creator_type()
            to_parse.on_kijiji_from()
            to_parse.listing()
            to_parse.website_url()
            to_parse.avg_reply()
            to_parse.reply_rate()

            to_parse.ad_id()
            to_parse.location()
            to_parse.title()
            to_parse.address()
            to_parse.published_date()
            to_parse.price()
            to_parse.description()

            to_parse.hydro_heat_water()
            to_parse.wifi()
            to_parse.parking()
            to_parse.agreement_type()
            to_parse.move_in_date()
            to_parse.pet_friendly()

            to_parse.size()
            to_parse.furnished()
            to_parse.appliances()
            to_parse.air_condition()
            to_parse.outdoor()
            to_parse.smoking()

            
        except Exception as ex:
            print(f'--- exc in link_scraper {ex} ---')
        finally:
            driver.quit()
            driver.close()