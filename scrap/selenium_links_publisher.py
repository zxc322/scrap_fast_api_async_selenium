from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constant import *
from selenium.webdriver.common.by import By

class LinkPublisher():

    def __init__(self):
        self.chanel = connection.channel()
        self.chanel.queue_declare('items_urls')

    def link_scraper(self, url):
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
                print(elem.get_attribute('href'))
                self.chanel.basic_publish(exchange='',
                    routing_key='items_urls',
                    body=elem.get_attribute('href'))
            
        except Exception as ex:
            print(f'--- exc in link_scraper {ex} ---')
        finally:
            driver.quit()
            driver.close()

