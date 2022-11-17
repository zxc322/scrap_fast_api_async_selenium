import pika
from selenium import webdriver

credentials = pika.PlainCredentials('zxc', 'zxc')
parameters = pika.ConnectionParameters('rabbitmq-host', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

options = webdriver.ChromeOptions()    
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])



LOCATIONS = {
    1: ('city-of-toronto', 'c37l1700273'),
    2: ('ville-de-quebec', 'c34l1700124'),
    3: ('nova-scotia', 'c37l9002'), 
    4: ('new-brunswick', 'c37l9005'), 
    5: ('manitoba', 'c37l9006'),
    6: ('british-columbia', 'c37l9007'),
    7: ('prince-edward-island', 'c37l9011'),
    8: ('saskatchewan' 'c37l9009'),
    9: ('alberta', 'c37l9003'),
    10: ('newfoundland', 'c37l9008')
    
}