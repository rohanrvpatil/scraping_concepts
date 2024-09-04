#scraping logic

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException

import unidecode
import traceback
import time
import random

from src import (config_driver)

#to extract value and initialise as "Value not found" if the value is not found
def safe_extract(driver, by, value, is_text,timeout=10, placeholder="Value not found"):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        if is_text==1:
            return element.text.strip()
        else:
            return element
    except Exception as e:
        print(f"Type: {type(e)}")
        #traceback.print_exc()
        return placeholder

def preprocess_title(text):
    
    title_bytes = text.encode('utf-8')
    decoded_title = title_bytes.decode('utf-8')
    title_string = unidecode.unidecode(decoded_title)
    
    return title_string
    
    
def preprocess_about_this_item(about_ul_element):
    
    if isinstance(about_ul_element, str):
        return about_ul_element #about_ul_element contains "Value not found"
 
    li_elements = about_ul_element.find_elements(By.TAG_NAME, 'li')
    about_items = [li.text.strip() for li in li_elements]
    about_items_string = " | ".join(about_items)
    
    about_items_bytes = about_items_string.encode('utf-8')
    decoded_string = about_items_bytes.decode('utf-8')
    about_items_string = unidecode.unidecode(decoded_string)
    
    return about_items_string

def preprocess_technical_details_summary(technical_details_summary):
    
    if isinstance(technical_details_summary, str):
        return technical_details_summary #technical_details_summary contains "Value not found"
    
    rows = technical_details_summary.find_elements(By.TAG_NAME, 'tr')
    data = []
    for row in rows:
        th_elements = row.find_elements(By.TAG_NAME, 'th')
        td_elements = row.find_elements(By.TAG_NAME, 'td')
        if th_elements and td_elements:
            th_text = th_elements[0].text.strip()
            td_text = td_elements[0].text.strip()
            data.append(f"{th_text}: {td_text}")
    td_summary = " | ".join(data)
    return td_summary


def get_next_page(driver):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 's-pagination-next') and text()='Next']"))
        )
        next_button.click()
        time.sleep(random.uniform(2, 5))
        return True
    except TimeoutException:
        print("No more pages available.")
        return False

def scrape_page(driver, ws):
    h2_elements = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2'))
    )

    h2_links = []
    for index, h2 in enumerate(h2_elements):
        try:
            link = h2.find_element(By.TAG_NAME, 'a').get_attribute('href')
            h2_links.append(link)
        except NoSuchElementException:
            print(f"No 'a' tag found within the h2 element at index {index}")

    while h2_links:
        num_requests = random.randint(5, 10)
        
        for _ in range(num_requests):
            if not h2_links:
                break
            
        
            link = h2_links.pop(0)
            driver.get(link)
            driver.implicitly_wait(7)

            price = safe_extract(driver, By.CLASS_NAME, "a-price.a-text-price.a-size-medium.apexPriceToPay", 1)
            title = preprocess_title(safe_extract(driver, By.ID, 'productTitle', 1))
            brand = safe_extract(driver, By.CLASS_NAME, "a-size-base.po-break-word", 1)
            model_name = safe_extract(driver, By.CSS_SELECTOR, "tr.po-model_name span.po-break-word", 1)
            screen_size = safe_extract(driver, By.CSS_SELECTOR, "tr.po-display\\.size span.po-break-word", 1)
            about_items_string = preprocess_about_this_item(safe_extract(driver, By.CSS_SELECTOR, 'ul.a-unordered-list.a-vertical.a-spacing-mini', 0))
            td_summary = preprocess_technical_details_summary(safe_extract(driver, By.ID, 'productDetails_techSpec_section_1', 0))
            rating = safe_extract(driver, By.CSS_SELECTOR, 'span[data-hook="rating-out-of-text"]', 1).split(' ')[0]

            new_row = [link, title, price, brand, model_name, screen_size, about_items_string, td_summary, rating]
            ws.append(new_row) 

            time.sleep(random.uniform(3, 7))
        
        driver.quit()
        time.sleep(random.uniform(2, 5))
        driver = config_driver()
    