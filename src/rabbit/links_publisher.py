import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import pika
from rabbit.pika_connect import parameters


class RabbitLinksPublisher:

    def __init__(self) -> None:
        connection = pika.BlockingConnection(parameters)
        self.chanel = connection.channel()
        self.chanel.queue_declare('items_urls')


    def send_message(self, body):
        self.chanel.basic_publish(exchange='',
                    routing_key='items_urls',
                    body=body)