import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
import sys, os
from selenium_items_scraper import ItemScraper
from rabbit.links_consumer import RabbitLinksConsumer

executor = ThreadPoolExecutor(5)
loop = asyncio.get_event_loop()


class ItemLoop:

    def __init__(self) -> None:
        self.item_scaper = ItemScraper()
        #self.rabbit_consumer = RabbitLinksConsumer()

    def scrape(self, url, *, loop):
        loop.run_in_executor(executor, self.item_scaper.item_scraper, url)


item = ItemLoop()


def callback(ch, method, properties, url):
        url = url.decode("utf-8")
        print(f'--- consume msg {url} --- ')
        url += '?siteLocale=en_CA' # To prevent Franch pages
        item.scrape(url, loop=loop)

if __name__ == '__main__':
    try:
        RabbitLinksConsumer().consume(callback=callback)
        loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
