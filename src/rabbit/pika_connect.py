import pika
from selenium import webdriver

credentials = pika.PlainCredentials('zxc', 'zxc')
parameters = pika.ConnectionParameters('rabbitmq-host', 5672, '/', credentials)


