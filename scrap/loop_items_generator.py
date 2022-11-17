import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
import sys, os
from selenium_links_consumer import LinkConsumer

executor = ThreadPoolExecutor(7)
loop = asyncio.get_event_loop()


class ItemLoop:

    def __init__(self) -> None:
        self.link_consumer = LinkConsumer()
    

    def scrape(self, url, *, loop):
        loop.run_in_executor(executor, self.link_consumer.item_scraper, url)

    def consume(self):
        self.link_consumer.chanel.basic_consume(
            queue='items_urls', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.link_consumer.chanel.start_consuming()


item = ItemLoop()
def callback(ch, method, properties, url):
        url = url.decode("utf-8")
        url += '?siteLocale=en_CA' # To prevent Franch pages
        item.scrape(url, loop=loop)


if __name__ == '__main__':
    try:
        item.consume()
        loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
