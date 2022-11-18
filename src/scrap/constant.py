import asyncio
import functools
from selenium import webdriver


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
    8: ('saskatchewan', 'c34l9009'),
    9: ('alberta', 'c37l9003'),
    10: ('newfoundland', 'c37l9008')
    
}

def sync(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.get_event_loop().run_until_complete(f(*args, **kwargs))
    return wrapper