import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from constant import LOCATIONS
from scrap.selenium_link_scraper import LinkScraper

executor = ThreadPoolExecutor(5)
loop = asyncio.get_event_loop()

class UrlsLoop:
    
    def __init__(self) -> None:
        self.province = self.input_province()
        self.page_urls = self.link_generator()
        self.link_scraper = LinkScraper()


    def input_province(self):
        print('Chose location as single number...')
        for k, v in LOCATIONS.items():
            print(f'{k} => {v}')

        while True:
            province_id = int(input('Number (0<n<11): '))
            if province_id > 0 and province_id < 11:
                break
        return LOCATIONS.get(province_id)

    def link_generator(self):
         return ('https://www.kijiji.ca/b-real-estate/{}/page-{}/{}?siteLocale=en_CA'.format(
            self.province[0], page, self.province[1]) for page in range(1, 2))

    def scrape(self, url, *, loop):
        loop.run_in_executor(executor, self.link_scraper.scraper, url)

            

province = UrlsLoop()

for page in province.page_urls:
    province.scrape(page, loop=loop)

loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))