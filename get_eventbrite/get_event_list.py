from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from common.start_webdriver_2 import start_driver_2
from get_eventbrite.cities import web3event_cities
from get_eventbrite.tags import web3event_tags

def get_event_list(url):
    url = url
    driver = start_driver_2()
    driver.get(url)
    delay = 3
    time.sleep(delay)
    dom = bs(driver.page_source, "html.parser")
    event_list = []
    
    return