import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from rabbit.pika_connect import parameters
import pika

class RabbitDataPublisher:

    def __init__(self) -> None:
        connection = pika.BlockingConnection(parameters)
        self.chanel = connection.channel()

    def send_message(self, body):
        self.chanel.queue_declare('items_data')
        self.chanel.basic_publish(exchange='',
                    routing_key='items_data',
                    body=body,
                    properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))