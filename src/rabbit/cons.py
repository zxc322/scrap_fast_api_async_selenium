#!/usr/bin/env python
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from scrap.constant import connection

def main():

    channel = connection.channel()
    channel2 = connection.channel()

    channel.queue_declare(queue='Q2')
    channel2.queue_declare(queue='Q3')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        channel2.basic_publish(exchange='', routing_key='Q3', body=body)
        print(f'redirec {body} to Q3')

    channel.basic_consume(queue='Q2', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

