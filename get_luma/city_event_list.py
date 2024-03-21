from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from common.categories_list import web3_categories_list
from common.start_webdriver_2 import start_driver_2
from common.utils import check_keywords_in_title
import time


def get_event_list(href):
    url = href
    driver = start_driver_2()
    driver.get(url)
    delay = 3
    time.sleep(delay)
    print("Page Loaded Completely")
    # while driver.execute_script("return document.readyState") != "complete":
    #      time.sleep(delay)
    data_list = []
    try:
        # WebDriverWait(driver, 5).until( EC.visibility_of_element_located((By.CSS_SELECTOR, "div.timeline")) )
        card_wrappers = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card-wrapper')))

        for card_wrapper in card_wrappers:
            unit_data = {}
            
            try:
                a_tag = card_wrapper.find_element(By.CSS_SELECTOR, 'a.event-link')
                unit_data['href'] = a_tag.get_attribute('href')

                h3_tag = card_wrapper.find_element(By.CLASS_NAME, 'jsx-3851280986')
                unit_data['title'] = h3_tag.text
                
                pill_labels = card_wrapper.find_elements(By.CLASS_NAME, 'jsx-146954525.pill-label')
                pill_label_texts = [label.text for label in pill_labels]
                unit_data['tags'] = pill_label_texts
                isIncluded = check_keywords_in_title(unit_data['title'], web3_categories_list)
                if(isIncluded):
                    data_list.append(unit_data)
            except NoSuchElementException:
                print("Unalbe to locate elements in card-wrapper")
        # print("222", data_list)
    except TimeoutException:
        print("Timed out waiting for time line to load")  
    except Exception as e:
        print(f'error: {e}')

    return data_list