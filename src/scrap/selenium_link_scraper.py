import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from scrap.constant import options
from rabbit.links_publisher import RabbitLinksPublisher


class LinkScraper():

    def __init__(self):
        self.rabbit = RabbitLinksPublisher()

    def scraper(self, url):
        try:
            print('--- parsing links... ---')
            driver = Remote(
                command_executor='http://chrome:4444/wd/hub',
                options=options,
                desired_capabilities=DesiredCapabilities.CHROME
                )       

            driver.get(url)      
            items_urls = driver.find_elements(By.XPATH,
                "//div[@class='info-container']/div[@class='title']/a")

            for elem in items_urls:
                url = elem.get_attribute('href')
                print(url)
                self.rabbit.send_message(url)
            
        except Exception as ex:
            print(f'--- exc in link_scraper {ex} ---')
        finally:
            driver.quit()
            driver.close()

