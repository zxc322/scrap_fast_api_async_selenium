import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import pika

from rabbit.pika_connect import parameters


class RabbitLinksConsumer:

    def __init__(self) -> None:
        connection = pika.BlockingConnection(parameters)
        self.chanel = connection.channel()


    def consume(self, callback):
        self.chanel.queue_declare('items_urls')
        self.chanel.basic_consume(
            queue='items_urls', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.chanel.start_consuming()
