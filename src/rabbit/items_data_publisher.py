import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from rabbit.pika_connect import parameters
import pika

class RabbitDataPublisher:

    # def __init__(self) -> None:
    #     self.chanel = connection.channel()
    #     self.chanel.queue_declare('items_data')

    @staticmethod
    def send_message(body):
        connection = pika.BlockingConnection(parameters)
        my_chanel = connection.channel()
        my_chanel.queue_declare('items_data')
        my_chanel.basic_publish(exchange='',
                    routing_key='items_data',
                    body=body,
                    properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))