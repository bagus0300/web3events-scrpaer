from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.start_webdriver_2 import start_driver_2
from get_luma.city_event_list import get_event_list
from common.utils import remove_repeated_events
from get_luma.event_detail_info import get_event_detailinfo


def get_from_luma():
    driver = start_driver_2()
    luma_url = 'https://lu.ma'
    driver.get(luma_url+'/explore')
    WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, "div.can-divide")) )
    event_list_values = []

    event_sections = driver.find_elements(By.CSS_SELECTOR, 'div.can-divide')
    city_event_elements = event_sections[0].find_elements(By.TAG_NAME, 'a')
    calendar_event_elements = event_sections[1].find_elements(By.TAG_NAME, 'a')

    city_event_href_values = [element.get_attribute('href') for element in city_event_elements]
    for city_href in city_event_href_values:
        event_list_values.extend(get_event_list(city_href))
    
    calendar_event_href_values = [element.get_attribute('href') for element in calendar_event_elements]
    for calendar_href in calendar_event_href_values:
        event_list_values.extend(get_event_list(calendar_href))

    filtered_event_list = remove_repeated_events(event_list_values, "href")
    print("count:", len(filtered_event_list))

    event_detail_list = [get_event_detailinfo(event) for event in filtered_event_list]
    return event_detail_list